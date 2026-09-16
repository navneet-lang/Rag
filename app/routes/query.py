import os
from dotenv import load_dotenv
from fastapi import APIRouter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from pydantic import BaseModel

load_dotenv()

router = APIRouter(prefix="/query", tags=["query"])

class QueryRequest(BaseModel):
    question: str

embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")

# YAHAN ADD KARNA HAI:
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")

vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    collection_name="sample_collection",
    url=QDRANT_URL,
)

@router.post("/")
async def query_endpoint(payload: QueryRequest):
    search_results = vector_db.similarity_search(query=payload.question, k=3)
    
    formatted_results = [
        {
            "content": doc.page_content,
            "page": doc.metadata.get("page", 0)
        }
        for doc in search_results
    ]
    
    return {
        "question": payload.question,
        "results": formatted_results
    }