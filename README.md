# Medical PDF RAG Application (GenAI Project)

This project is a Retrieval-Augmented Generation (RAG) application that allows users to ask questions from a medical book PDF using LLMs.

Built using:
LangChain
Mistral AI
ChromaDB
HuggingFace Embeddings
Streamlit

---

## Features

Upload medical knowledge into vector database
Ask questions in natural language
Answers generated using LLM
Efficient semantic search using embeddings
Persistent vector database using ChromaDB
Simple Streamlit UI

---

## Tech Stack

Python
LangChain
Mistral AI (LLM)
HuggingFace sentence-transformers
ChromaDB (Vector Database)
Streamlit (UI)

---

## Project Structure

```
app.py → Streamlit UI
rag_pipeline.py → RAG pipeline logic
data/ → medical PDF
chroma_db/ → vector database
requirements.txt → dependencies
```

---

## How it works

1. PDF is loaded and split into smaller chunks
2. Each chunk converted into embedding vector
3. Vectors stored in ChromaDB
4. User question converted into embedding
5. Similar chunks retrieved
6. Context sent to Mistral LLM
7. LLM generates answer

---

## Installation

Clone repository:

```bash
git clone https://github.com/yourusername/medical-rag.git
cd medical-rag
```

Create virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Add .env file:

```
MISTRAL_API_KEY=your_key_here
HF_TOKEN=your_token_here
```

---

## Run Application

```bash
streamlit run app.py
```

---

## Example Questions

What is diabetes?
What is hypertension?
Symptoms of asthma?
What causes cancer?

---

## Learning Outcomes

Built end-to-end RAG pipeline
Understood embeddings and vector databases
Learned prompt engineering basics
Integrated LLM into application
Built Streamlit UI
Used GitHub for version control

---

## Future Improvements

Chat interface
Multiple PDF support
Deploy on cloud
Add conversation memory
Use better embedding models
