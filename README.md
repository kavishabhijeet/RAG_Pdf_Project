# Medical PDF Question Answering System (RAG)

## Project Overview

This project is an AI-powered Question Answering system that allows users to upload medical PDF documents and ask questions in natural language.

The system uses Retrieval-Augmented Generation (RAG) to provide accurate answers based only on the uploaded document content.

This helps in quickly finding important information from lengthy medical PDFs.

---

## Features

* Upload medical PDF
* Ask questions in natural language
* Context-based answers using LLM
* Uses embeddings for semantic search
* Streamlit user interface
* Fast and efficient retrieval

---

## Tech Stack

Python
LangChain
HuggingFace Embeddings
Chroma Vector Database
Streamlit
LLM (Mistral / OpenAI)

---

## How It Works (RAG Pipeline)

1. User uploads PDF
2. PDF text is extracted
3. Text is split into chunks
4. Chunks converted into embeddings
5. Stored in vector database
6. User asks question
7. Relevant chunks retrieved
8. LLM generates final answer

---

## Project Structure

medical-pdf-rag-chatbot

app.py → Streamlit UI
requirements.txt → dependencies
sample_data → sample pdf
screenshots → project images

---

## How to Run Project

1. Clone repository

git clone https://github.com/your-username/medical-pdf-rag-chatbot

2. Install dependencies

pip install -r requirements.txt

3. Run app

streamlit run app.py

---

## Sample Questions

What are the symptoms of diabetes?
What treatment is suggested?
What precautions are mentioned?

---

## Future Improvements

Chat history memory
Multiple PDF support
Source citation display
Improved UI

---

## Author

Abhijeet Anand
Aspiring Data Analyst & GenAI Developer
