from pathlib import Path
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter


load_dotenv()
pdf_path = Path(__file__).parent / "data" / "COMPUTER NETWORKS NOTES.pdf"

# PDF Loader
loader = PyPDFLoader(str(pdf_path))
docs = loader.load()



#splition pdf 

text_splitter =  RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap = 400
)
  
chunks = text_splitter.split_documents(documents=docs)

# embding  model
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

# 4. Automatically Creates Collection & Adds Documents
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="sample_collection"
)

print("Vector store created and documents embedded successfully.")


#https://f28b9454-2f95-40cc-b000-76fc3abece36.eu-central-1-0.aws.cloud.qdrant.io
