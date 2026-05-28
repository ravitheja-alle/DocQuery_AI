from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Headless Document Intelligence API for PDF extraction, vectorization, and RAG.",
    docs_url="/docs",
    redoc_url=None,
)

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": settings.PROJECT_NAME}