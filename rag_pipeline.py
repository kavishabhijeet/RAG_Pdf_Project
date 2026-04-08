from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader("data\ENCYCLOPEDIA_OF_MEDICINE.pdf")
pages = loader.load()
print(f"Total Pages : {len(pages)}")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 100
)

docs = text_splitter.split_documents(pages)
print(f"Total Chunk Pages : {len(docs)}")