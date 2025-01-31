# 🤖 RAG PDF Assistant: Powered by 🏆 `DeepSeek-R1` ~ 1.5B , `Ollama`, `Streamlit` & `FAISS`

![author](https://img.shields.io/badge/author-mohd--faizy-red)
![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-0C0D0E?logo=ollama&logoColor=white)
![PDFPlumber](https://img.shields.io/badge/PDFPlumber-FF0000?logo=pdf&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-00ADD8?logo=langchain&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD43B?logo=huggingface&logoColor=black)
![FAISS](https://img.shields.io/badge/FAISS-00A98F?logo=faiss&logoColor=white)


![Demo]()

AI-powered chatbot designed specifically for interactive document retrieval from PDFs. This project leverages the capabilities of **DeepSeek-R1 (1.5B parameters)** alongside **Streamlit** for a user-friendly interface, **Ollama** for model serving, and **FAISS** for efficient vector search and retrieval, creating a seamless experience for extracting and querying knowledge from uploaded PDF documents.

![Demo]()

---

## 📁 Detailed Directory Structure

```

RAG-DeepSeek/
├── app/
│   ├── __init__.py          # Python package initialization file
│   ├── main.py              # Main Streamlit application file where the chat interface is defined
│   ├── utils.py             # Contains helper functions for document processing, embedding, and retrieval
├── assets/                  # Folder for storing static files like images, CSS, etc.
├── requirements.txt         # Lists all Python dependencies needed for the project
├── .gitignore               # Specifies files to be ignored by Git
├── README.md                # This README file with detailed project information

```

---

## 🚀 Quick Start Guide

### Prerequisites

- **Python 3.9 or higher**: Ensure you have Python installed on your system.
- **Ollama**: Download and install Ollama from [here](https://ollama.ai/). Make sure it's running before proceeding.
- **DeepSeek-R1 Model**: Pull the model using:
- 
  ```bash
  ollama pull deepseek-r1:1.5b
  ```

### Installation Steps

1. __Clone the Repository__:

   ```bash
   git clone https://github.com/mohd-faizy/RAG-DeepSeek.git
   ```

2. __Navigate to the Project Directory__:

   ```bash
   cd RAG-DeepSeek
   ```

3. __Setup Virtual Environment__:

   ```bash
   python -m venv venv
   ```

4. __Activate the Virtual Environment__:
   - __For Linux/macOS__:

     ```bash
     source venv/bin/activate
     ```

   - __For Windows__:

     ```bash
     .\venv\Scripts\activate
     ```

5. __Install Required Dependencies__:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🖥️ Usage Instructions

1. __Start Ollama Service__:

   ```bash
   ollama serve
   ```

2. __Launch the Chat Interface__:
   In another terminal window, run:

   ```bash
   streamlit run app/main.py
   ```

   This will open the Streamlit app in your default web browser where you can interact with the chatbot.

---

## 🔧 Troubleshooting Guide

### Port Conflict (11434)

If you encounter issues with port 11434 being in use:

- __For Windows__:

  ```bash
  netstat -ano | findstr :11434
  taskkill /PID <PID> /F
  ```

- __For Linux/macOS__:

  ```bash
  lsof -i :11434
  kill -9 <PID>
  ```

### Common Issues

- Ensure that the Ollama service is actively running before you start the Streamlit application.
- Verify the installation of the DeepSeek-R1 model by running `ollama list`.
- If there are connection issues, review your firewall settings to allow necessary ports.

## 🍰 Contributing

Contributions are welcome!

## ⚖ ➤ License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

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
