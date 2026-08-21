# --- Stage 1: build the Vue frontend -------------------------------------
FROM node:22-slim AS frontend-build
WORKDIR /app/frontend
COPY frontend/package.json frontend/package-lock.json* ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

# --- Stage 2: FastAPI backend, serving the built frontend as static ------
FROM python:3.12-slim
WORKDIR /app

COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ ./
COPY --from=frontend-build /app/frontend/dist ./static

# Data directory for the SQLite DB and uploaded images. Mount a Railway
# volume at /data (see DATABASE_URL / UPLOADS_DIR below) so it survives
# redeploys; without a volume this still works but resets on every deploy.
ENV DATABASE_URL=sqlite:////data/portfolio.db
ENV UPLOADS_DIR=/data/uploads
RUN mkdir -p /data

EXPOSE 8000
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]
