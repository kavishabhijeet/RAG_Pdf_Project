import os
from dotenv import load_dotenv
load_dotenv()
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# STEP 1 — Load PDF
loader = PyPDFLoader(r"data\ENCYCLOPEDIA_OF_MEDICINE.pdf")
pages = loader.load()
print(f"Total Pages : {len(pages)}")

# STEP 2 — Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 100
)

docs = text_splitter.split_documents(pages)
print(f"Total Chunk Pages : {len(docs)}")

# Load Embedding Models
embedding_model = HuggingFaceEmbeddings(model_name= "sentence-transformers/all-MiniLM-L6-v2")

# Store embeddings in chromaDB
vectore_store = Chroma.from_documents(documents=docs, embedding= embedding_model, persist_directory="chroma_db")
vectore_store.persist()

print("Embeddings store in ChromaDB successfully")