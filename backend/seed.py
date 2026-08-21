"""Populate a fresh database (e.g. a new Railway volume) with the current
project catalog. Safe to re-run: skips any slug that already exists, and
only copies an image into UPLOADS_DIR if it isn't already there.

Usage: python seed.py
"""
import json
import os
import shutil

from models import Project, SessionLocal, create_tables

SEED_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOADS_DIR = os.environ.get("UPLOADS_DIR", os.path.join(SEED_DIR, "uploads"))
SEED_UPLOADS_DIR = os.path.join(SEED_DIR, "seed_uploads")


def copy_seed_image(url):
    """url is a '/uploads/xxx.png' reference; copy the matching file from
    seed_uploads/ into UPLOADS_DIR if it's not already there."""
    if not url or not url.startswith("/uploads/"):
        return
    filename = url.removeprefix("/uploads/")
    src = os.path.join(SEED_UPLOADS_DIR, filename)
    dst = os.path.join(UPLOADS_DIR, filename)
    if os.path.isfile(dst) or not os.path.isfile(src):
        return
    os.makedirs(UPLOADS_DIR, exist_ok=True)
    shutil.copyfile(src, dst)


def main():
    create_tables()
    db = SessionLocal()
    try:
        with open(os.path.join(SEED_DIR, "seed_data.json"), encoding="utf-8") as f:
            projects = json.load(f)

        added = 0
        for data in projects:
            if db.query(Project).filter(Project.slug == data["slug"]).first():
                continue
            copy_seed_image(data.get("thumbnail"))
            copy_seed_image(data.get("arch_diagram"))
            db.add(Project(**data))
            added += 1

        db.commit()
        print(f"Seeded {added} project(s), skipped {len(projects) - added} already present.")
    finally:
        db.close()


if __name__ == "__main__":
    main()
