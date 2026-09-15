from fastapi import FastAPI
from app.routes.query import router as query_router


app= FastAPI(
    title="Rag API",
    description="This is a Rag API",
    version="0.1.0",
)  

app.include_router(query_router)