# 📄 AI-Powered PDF Question Answering System using RAG

An intelligent **Retrieval-Augmented Generation (RAG)** application that enables users to upload PDF documents and ask questions in natural language. The system retrieves the most relevant document sections using semantic search powered by **Google Gemini Embeddings** and **Qdrant Vector Database**.

---

## 🚀 Features

* Upload PDF documents
* Automatic PDF text extraction
* Intelligent document chunking
* Semantic embedding generation using Google Gemini
* Fast similarity search using Qdrant Vector Database
* Interactive Streamlit web interface
* Retrieve the most relevant document chunks based on user queries

---

## 🛠 Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI / LLM

* LangChain
* Google Gemini Embeddings

### Vector Database

* Qdrant

### Document Processing

* PyPDF
* Recursive Character Text Splitter

---

## 📂 Project Structure

```
PDF-RAG-QA-System/
│
├── app.py
├── requirements.txt
├── .gitignore
├── uploads/
├── README.md
└── venv/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/PDF-RAG-QA-System.git

cd PDF-RAG-QA-System
```

### Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Qdrant

If using Docker

```bash
docker run -p 6333:6333 qdrant/qdrant
```

---

## Run Application

```bash
streamlit run app.py
```

---

## How It Works

1. Upload a PDF document.
2. The PDF is converted into pages.
3. Pages are split into smaller chunks.
4. Google Gemini generates vector embeddings.
5. Embeddings are stored in Qdrant.
6. User enters a question.
7. Similarity search retrieves the top relevant chunks.
8. Retrieved chunks are displayed to the user.

---

## Project Workflow

```
PDF Upload
      │
      ▼
Load PDF using PyPDF
      │
      ▼
Split into Chunks
      │
      ▼
Generate Gemini Embeddings
      │
      ▼
Store in Qdrant
      │
      ▼
User Question
      │
      ▼
Similarity Search
      │
      ▼
Relevant Chunks Retrieved
```

---

## Skills Demonstrated

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Databases
* Embedding Models
* LangChain
* Google Gemini API
* Streamlit
* Python
* Document Processing
* Information Retrieval

---

## Future Enhancements

* Generate natural language answers using Gemini LLM
* Support multiple PDF uploads
* Chat history
* Source citation
* Hybrid search (Keyword + Vector)
* Persistent vector storage
* Authentication
* Cloud deployment (Render/AWS/Azure)

---

## Sample Use Cases

* Research paper analysis
* Company policy search
* Resume and portfolio assistant
* Educational PDF chatbot
* Legal document search
* Technical documentation assistant

---

## Author

**Akhila Jampala**

Python | AI | Generative AI | LangChain | Machine Learning | Backend Development
