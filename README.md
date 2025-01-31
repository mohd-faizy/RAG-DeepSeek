# 🤖 RAG PDF Assistant: Powered by 🏆 `DeepSeek-R1` ~ 1.5B , `Ollama`, `Streamlit` & `FAISS`

![author](https://img.shields.io/badge/author-mohd--faizy-red)
![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-0C0D0E?logo=ollama&logoColor=white)
![PDFPlumber](https://img.shields.io/badge/PDFPlumber-FF0000?logo=pdf&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-00ADD8?logo=langchain&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD43B?logo=huggingface&logoColor=black)
![FAISS](https://img.shields.io/badge/FAISS-00A98F?logo=faiss&logoColor=white)

---

## 🌟 **Overview**  

**RAG PDF Assistant** is an AI-powered **Retrieval-Augmented Generation (RAG)** chatbot that enables **intelligent PDF document search and retrieval.** It combines:  

✅ **DeepSeek-R1 (1.5B)** – Advanced AI-powered language model for **accurate responses.**  
✅ **FAISS** – Fast vector search for **efficient document retrieval.**  
✅ **Ollama** – Lightweight model serving and **seamless inference.**  
✅ **LangChain** – Modular AI framework for **query execution and reasoning.**  
✅ **Streamlit** – Intuitive and interactive **web-based UI.**  

### 🎯 **Use Cases**  

🔍 **Quickly search** through large PDF documents.  
📄 **Summarize reports, research papers, contracts,** and more.  
📘 **Extract relevant information** with AI-driven accuracy.  
🤖 **Ask natural language questions** and get concise answers.  

---

## 🚀 **Demo Screenshots**  

### **📌 UI Preview**  

![Demo](https://github.com/mohd-faizy/RAG-DeepSeek/blob/main/assets/rag-pdf-retv.png?raw=true)  

### **📌 Application Workflow**  

![Workflow](https://github.com/mohd-faizy/RAG-DeepSeek/blob/main/assets/RAG-app-flow.png?raw=true)  

---

## 🛠️ **Installation & Setup**  

### **🔧 Prerequisites**  

Ensure you have the following installed:  

- **Python 3.9+**  
- **pip** (Python package manager)  
- **Git** (for cloning the repository)  

### **📥 Step 1: Clone the Repository**  

```bash
$ git clone https://github.com/mohd-faizy/RAG-DeepSeek.git
$ cd RAG-DeepSeek
```

### **📦 Step 2: Install Dependencies**  

```bash
$ pip install -r requirements.txt
```

### **⚙️ Step 3: Run the Application**  

1. Start Ollama service:

   ```bash
   ollama serve
   ```

2. In a separate terminal, launch the chat interface:

   ```bash
   streamlit run app/main.py
   ```

The application will launch in your browser at `http://localhost:0000/`.  

---

## 📁 **Directory Structure**  

```plaintext
RAG-DeepSeek/
├── app/
│   ├── __init__.py          # Python package initialization
│   ├── main.py              # Main Streamlit application file
│   ├── utils.py             # Utility functions for PDF processing, embeddings, retrieval
├── assets/                  # Static files like images, CSS, etc.
├── requirements.txt         # Python dependencies
├── .gitignore               # Files ignored by Git
├── README.md                # Project documentation
```

---

## 🧠 **How It Works**  

1️⃣ **Upload a PDF** → The AI extracts and indexes the content.  
2️⃣ **Ask a question** → The system searches for the most relevant passages.  
3️⃣ **AI answers your query** → Based on retrieved document content.  

🔹 **Uses FAISS** for **fast, efficient document retrieval.**  
🔹 **DeepSeek-R1** ensures **high-quality, context-aware answers.**  

---

## 🔗 **Technologies Used**  

| **Technology**  | **Purpose**  |
|---------------|-------------|
| **DeepSeek-R1 (1.5B)** | Language model for intelligent responses |
| **Ollama** | Model serving and inference |
| **FAISS** | Vector search for document retrieval |
| **LangChain** | AI-driven reasoning and query handling |
| **Streamlit** | User-friendly web interface |
| **PDFPlumber** | Extracting text from PDFs |

---


### **🤝 Steps to Contribute**  

1. Fork the repository  
2. Create a new feature branch (`git checkout -b feature-name`)  
3. Commit your changes (`git commit -m "Added new feature"`)  
4. Push to your fork (`git push origin feature-name`)  
5. Open a pull request  

---

## ⚖ ➤ License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.  

## ❤️ Support

If you find this repository helpful, show your support by starring it! For questions or feedback, reach out on [Twitter(`X`)](https://twitter.com/F4izy).

## 🔗Connect with me

➤ If you have questions or feedback, feel free to reach out!!!

[<img align="left" src="https://cdn4.iconfinder.com/data/icons/social-media-icons-the-circle-set/48/twitter_circle-512.png" width="32px"/>][twitter]
[<img align="left" src="https://cdn-icons-png.flaticon.com/512/145/145807.png" width="32px"/>][linkedin]
[<img align="left" src="https://cdn-icons-png.flaticon.com/512/2626/2626299.png" width="32px"/>][Portfolio]

[twitter]: https://twitter.com/F4izy
[linkedin]: https://www.linkedin.com/in/mohd-faizy/
[Portfolio]: https://ai.stackexchange.com/users/36737/faizy?tab=profile

---

<img src="https://github-readme-stats.vercel.app/api?username=mohd-faizy&show_icons=true" width=380px height=200px />
