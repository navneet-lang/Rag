from fastapi import APIRouter

router = APIRouter(
    prefix="/query",
    tags=["query"],

)

@router.post("/")
async def query(question:str):
    return{"question":question, "answer":"This is a placeholder answer"}