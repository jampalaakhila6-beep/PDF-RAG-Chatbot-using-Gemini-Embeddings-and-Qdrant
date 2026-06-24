import streamlit as st
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore

st.set_page_config(page_title="PDF RAG")

st.title("📄 PDF RAG QA System")

# API Key
google_api_key = st.text_input(
    "Enter Google API Key",
    type="password"
)

if google_api_key:
    os.environ["GOOGLE_API_KEY"] = google_api_key

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file and google_api_key:

    # Save PDF
    pdf_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF Uploaded Successfully")

    # Load PDF
    loader = PyPDFLoader(pdf_path)

    pages = loader.load()

    st.write("Total Pages:", len(pages))

    # Chunking
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(pages)

    st.write("Total Chunks:", len(chunks))

    # Embeddings
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001"
    )

    # Store in Qdrant
    vector_store = QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        url="http://localhost:6333",
        collection_name="pdf_collection"
    )

    st.success("Vector Database Created")

    question = st.text_input(
        "Ask Question"
    )

    if question:

        retriever = QdrantVectorStore.from_existing_collection(
            embedding=embeddings,
            collection_name="pdf_collection",
            url="http://localhost:6333"
        )

        docs = retriever.similarity_search(
            question,
            k=3
        )

        st.subheader("Retrieved Chunks")

        for i, doc in enumerate(docs):
            st.write(f"Result {i+1}")
            st.write(doc.page_content)
            st.divider()