from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
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

os.makedirs("uploads", exist_ok=True)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

create_tables()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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
def reorder_projects(items: list[ReorderItem], db: Session = Depends(get_db)):
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
def create_project(data: ProjectCreate, db: Session = Depends(get_db)):
    p = Project(**data.model_dump())
    db.add(p)
    db.commit()
    db.refresh(p)
    return p


@app.put("/api/projects/{project_id}")
def update_project(project_id: int, data: ProjectUpdate, db: Session = Depends(get_db)):
    p = db.query(Project).filter(Project.id == project_id).first()
    if not p:
        raise HTTPException(status_code=404, detail="Not found")
    for k, v in data.model_dump().items():
        setattr(p, k, v)
    db.commit()
    db.refresh(p)
    return p


@app.delete("/api/projects/{project_id}", status_code=204)
def delete_project(project_id: int, db: Session = Depends(get_db)):
    p = db.query(Project).filter(Project.id == project_id).first()
    if not p:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(p)
    db.commit()


@app.post("/api/upload")
async def upload_file(file: UploadFile = File(...)):
    ext = os.path.splitext(file.filename)[1]
    filename = f"{uuid.uuid4().hex}{ext}"
    path = os.path.join("uploads", filename)
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"url": f"/uploads/{filename}"}
