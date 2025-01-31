import streamlit as st
import ollama
from utils import load_pdf, split_text, create_vector_store, retrieve_relevant_docs, save_temp_file, cleanup_temp_file

# Set Streamlit page config
st.set_page_config(
    page_title="📄 PDF Chat Assistant",
    page_icon="📄",
    layout="centered"
)

# Custom CSS for DeepSeek-like UI
st.markdown("""
    <style>
        body {
            background-color: #1E1E2E;
            color: #ECEFF4;
        }
        .thinking {
            background-color: #313244;
            border-left: 10px solid #F28FAD;
            padding: 12px;
            margin: 12px 0;
            font-size: 14px;
            font-style: italic;
            color: #C3BAC6;
            border-radius: 5px;
        }
        .header {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #F28FAD;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #A6ADC8;
            margin-bottom: 20px;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #888;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Display header
st.markdown('<div class="header">DocuQuery 🤖</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">RAG PDF Assistant: Efficient Document Search</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle" style="font-size: 13px;">Powered by 🏆 DeepSeek-R1:1.5B, Ollama, Streamlit & FAISS | by faizy</div>', unsafe_allow_html=True)

# Initialize session state
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "📄 Upload a PDF and ask any question about its content!"}
    ]

# Sidebar for PDF upload
st.sidebar.header("📂 Upload PDF")
uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    temp_file_path = save_temp_file(uploaded_file)
    
    # Load PDF and extract text
    docs = load_pdf(temp_file_path)
    
    # Chunk the text
    documents = split_text(docs)
    
    # Generate vector embeddings
    vector_store = create_vector_store(documents)
    st.session_state.vector_store = vector_store
    st.sidebar.success("✅ PDF processed successfully! You can now ask questions.")
    
    # Clean up the temporary file
    cleanup_temp_file(temp_file_path)

# Display chat messages immediately
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if "<think>" in msg["content"]:
            formatted_content = msg["content"].replace("<think>", '<div class="thinking">').replace("</think>", "</div>")
            st.markdown(formatted_content, unsafe_allow_html=True)
        else:
            st.markdown(msg["content"])

# User input for querying PDF content
user_input = st.chat_input("Ask a question about your PDF...")

if user_input:
    # Immediately display the user's question
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Process response only if vector store is ready
    if st.session_state.vector_store:
        with st.spinner("🧠 Thinking..."):
            relevant_docs = retrieve_relevant_docs(st.session_state.vector_store, user_input)

            if not relevant_docs or not relevant_docs[0].page_content.strip():
                answer = "I couldn't find any relevant content in the PDF. Try rephrasing your question."
            else:
                context = "\n".join([doc.page_content for doc in relevant_docs])

                response = ollama.chat(
                    model="deepseek-r1:1.5b",
                    messages=[
                        {"role": "system", "content": "You are an AI assistant helping users analyze and understand PDF documents. Provide clear, accurate, and professional responses based on the document content."},
                        {"role": "user", "content": f"Based on the provided document content, answer concisely and accurately:\n\n---\n{context}\n---\n\nQuestion: {user_input}"}
                    ]
                )
                answer = response["message"]["content"]

        st.session_state.messages.append({"role": "assistant", "content": answer})
        
        with st.chat_message("assistant"):
            if "<think>" in answer:
                formatted_answer = answer.replace("<think>", '<div class="thinking">').replace("</think>", "</div>")
                st.markdown(formatted_answer, unsafe_allow_html=True)
            else:
                st.markdown(answer)
