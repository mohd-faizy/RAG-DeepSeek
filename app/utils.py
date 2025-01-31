import os
from langchain_community.document_loaders import PDFPlumberLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings  
from langchain_community.vectorstores import FAISS

def load_pdf(file_path):
    """
    Load the content of a PDF file using PDFPlumberLoader.

    Args:
    file_path (str): Path to the PDF file.

    Returns:
    list: List of Document objects containing the PDF content.
    """
    loader = PDFPlumberLoader(file_path)
    return loader.load()

def split_text(documents, chunk_size=500, chunk_overlap=100):
    """
    Split documents into smaller chunks for processing.

    Args:
    documents (list): List of Document objects to split.
    chunk_size (int): Size of each chunk in characters.
    chunk_overlap (int): Overlap between chunks in characters.

    Returns:
    list: List of split Document objects.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_documents(documents)

def create_vector_store(documents, model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """
    Create a FAISS vector store from the documents using HuggingFace embeddings.

    Args:
    documents (list): List of Document objects to embed.
    model_name (str): Name of the HuggingFace model for embeddings.

    Returns:
    FAISS: Initialized FAISS vector store.
    """
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    return FAISS.from_documents(documents, embeddings)

def retrieve_relevant_docs(vector_store, query, k=3):
    """
    Retrieve the k most relevant documents from the vector store for a given query.

    Args:
    vector_store (FAISS): FAISS vector store to search.
    query (str): Query to search for.
    k (int): Number of documents to retrieve.

    Returns:
    list: List of k Document objects relevant to the query.
    """
    retriever = vector_store.as_retriever(search_kwargs={"k": k})
    return retriever.invoke(query)

def save_temp_file(uploaded_file):
    """
    Save an uploaded file temporarily to disk.

    Args:
    uploaded_file (UploadedFile): File uploaded through Streamlit.

    Returns:
    str: Path to the saved temporary file.
    """
    temp_file_path = "temp.pdf"
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getvalue())
    return temp_file_path

def cleanup_temp_file(file_path):
    """
    Clean up the temporary file from disk.

    Args:
    file_path (str): Path to the temporary file to remove.
    """
    if os.path.exists(file_path):
        os.remove(file_path)