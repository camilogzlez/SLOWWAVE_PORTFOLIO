from fastapi import FastAPI, Depends, Header, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel, field_validator
from typing import Optional
import shutil, os, uuid

from models import Project, SessionLocal, create_tables

app = FastAPI(title="Portfolio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:4173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# In production this points at the Railway volume mount (e.g. /data/uploads)
# so uploaded images survive redeploys.
UPLOADS_DIR = os.environ.get("UPLOADS_DIR", "uploads")
os.makedirs(UPLOADS_DIR, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=UPLOADS_DIR), name="uploads")

create_tables()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Shared secret gating every write endpoint (the admin UI's PIN screen sends
# it as X-Admin-Token). Left unset in local dev to skip the check; set
# ADMIN_TOKEN in Railway to actually lock these routes down in production.
ADMIN_TOKEN = os.environ.get("ADMIN_TOKEN")


def require_admin(x_admin_token: Optional[str] = Header(None, alias="X-Admin-Token")):
    if ADMIN_TOKEN and x_admin_token != ADMIN_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid admin token")


@app.get("/api/admin/ping")
def admin_ping(_: None = Depends(require_admin)):
    return {"ok": True}


class ProjectCreate(BaseModel):
    title: str
    slug: str
    category: str
    description: str
    long_description: Optional[str] = None
    tech_stack: list[str] = []
    thumbnail: Optional[str] = None
    video_url: Optional[str] = None
    arch_diagram: Optional[str] = None
    github_url: Optional[str] = None
    demo_url: Optional[str] = None
    year: Optional[str] = None
    team_size: Optional[int] = None
    tags: list[str] = []
    order: int = 0
    project_type: Optional[str] = "PERSONAL"

    @field_validator('video_url', 'arch_diagram', 'github_url', 'demo_url',
                     'thumbnail', 'long_description', 'year', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        return None if v == '' else v


class ProjectUpdate(ProjectCreate):
    pass


@app.get("/api/projects")
def list_projects(category: Optional[str] = None, db: Session = Depends(get_db)):
    q = db.query(Project)
    if category and category != "ALL":
        q = q.filter(Project.category == category)
    return q.order_by(Project.order).all()


class ReorderItem(BaseModel):
    id: int
    order: int

@app.put("/api/projects/reorder")
def reorder_projects(items: list[ReorderItem], db: Session = Depends(get_db), _auth: None = Depends(require_admin)):
    for item in items:
        db.query(Project).filter(Project.id == item.id).update({"order": item.order})
    db.commit()
    return {"ok": True}


@app.get("/api/projects/{slug}")
def get_project(slug: str, db: Session = Depends(get_db)):
    p = db.query(Project).filter(Project.slug == slug).first()
    if not p:
        raise HTTPException(status_code=404, detail="Not found")
    return p


@app.post("/api/projects", status_code=201)
def create_project(data: ProjectCreate, db: Session = Depends(get_db), _auth: None = Depends(require_admin)):
    p = Project(**data.model_dump())
    db.add(p)
    db.commit()
    db.refresh(p)
    return p


@app.put("/api/projects/{project_id}")
def update_project(project_id: int, data: ProjectUpdate, db: Session = Depends(get_db), _auth: None = Depends(require_admin)):
    p = db.query(Project).filter(Project.id == project_id).first()
    if not p:
        raise HTTPException(status_code=404, detail="Not found")
    for k, v in data.model_dump().items():
        setattr(p, k, v)
    db.commit()
    db.refresh(p)
    return p


@app.delete("/api/projects/{project_id}", status_code=204)
def delete_project(project_id: int, db: Session = Depends(get_db), _auth: None = Depends(require_admin)):
    p = db.query(Project).filter(Project.id == project_id).first()
    if not p:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(p)
    db.commit()


@app.post("/api/upload")
async def upload_file(file: UploadFile = File(...), _auth: None = Depends(require_admin)):
    ext = os.path.splitext(file.filename)[1]
    filename = f"{uuid.uuid4().hex}{ext}"
    path = os.path.join(UPLOADS_DIR, filename)
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"url": f"/uploads/{filename}"}


# --- Serve the built Vue frontend (single-service deploy) ---------------
# The Dockerfile builds the frontend and copies its `dist/` output here.
# In local dev (Vite dev server on :5173) this directory doesn't exist, so
# everything below is skipped and the API runs standalone as before.
STATIC_DIR = os.environ.get("STATIC_DIR", "static")

if os.path.isdir(STATIC_DIR):
    app.mount("/assets", StaticFiles(directory=os.path.join(STATIC_DIR, "assets")), name="assets")

    @app.get("/{full_path:path}")
    async def spa(full_path: str):
        # Serves any other built file at its exact path (favicon, images
        # referenced from index.html, ...); anything else -- including
        # client-side routes like /fr or /admin -- falls back to
        # index.html so vue-router can take over.
        candidate = os.path.join(STATIC_DIR, full_path)
        if full_path and os.path.isfile(candidate):
            return FileResponse(candidate)
        return FileResponse(os.path.join(STATIC_DIR, "index.html"))
