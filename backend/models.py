import os

from sqlalchemy import Column, Integer, String, Text, JSON, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# In production this points at the Railway volume mount (e.g.
# sqlite:////data/portfolio.db) so the database survives redeploys.
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./portfolio.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    slug = Column(String(200), unique=True, nullable=False)
    category = Column(String(100), nullable=False)  # WEB, BIGDATA, AI, DEVOPS
    description = Column(Text, nullable=False)
    long_description = Column(Text, nullable=True)
    tech_stack = Column(JSON, nullable=False, default=list)  # ["Python", "FastAPI", ...]
    thumbnail = Column(String(500), nullable=True)
    video_url = Column(String(500), nullable=True)  # YouTube or Loom share URL
    arch_diagram = Column(String(500), nullable=True)  # architecture diagram image URL
    github_url = Column(String(500), nullable=True)
    demo_url = Column(String(500), nullable=True)
    year = Column(String(10), nullable=True)
    team_size = Column(Integer, nullable=True)
    tags = Column(JSON, nullable=False, default=list)  # extra labels
    order = Column(Integer, default=0)
    project_type = Column(String(20), nullable=True, default="PERSONAL")  # SCHOOL | PERSONAL | PROFESSIONAL


def create_tables():
    Base.metadata.create_all(bind=engine)
