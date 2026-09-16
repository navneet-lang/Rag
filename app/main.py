from fastapi import FastAPI
from app.routes.query import router as query_router

app = FastAPI(
    title="RAG API",
    description="Vector Search & Retrieval API",
    version="0.1.0",
)

app.include_router(query_router)