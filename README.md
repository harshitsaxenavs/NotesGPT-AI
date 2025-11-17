# NoteGPT

NoteGPT is a lightweight, open‑source AI chatbot that allows you to
upload your PDF notes and chat with them using free embeddings and
OpenRouter LLM models.

## 🚀 Features

-   Upload any PDF and extract text automatically\
-   Uses **FAISS** for fast similarity search\
-   Uses **HuggingFace Embeddings (free)**\
-   LLM responses powered by **OpenRouter** (works with free models)\
-   Simple Streamlit UI\
-   Completely open‑source --- no paid API required

## 🛠️ Tech Stack

-   **Streamlit** -- UI\
-   **FAISS** -- Vector Database\
-   **HuggingFace** -- Embeddings\
-   **OpenRouter API** -- LLM text generation\
-   **PyPDF2** -- PDF text extraction

## 📦 Installation

``` bash
git clone https://github.com/your-username/NoteGPT
cd NoteGPT
pip install -r requirements.txt
```

## ▶️ Run the App

``` bash
streamlit run app.py
```

## 🔑 API Key (OpenRouter)

Get a free API key from:\
https://openrouter.ai

## 📁 Project Structure

    NoteGPT/
    │-- app.py
    │-- requirements.txt
    │-- README.md

## 📝 Usage

1.  Upload a PDF\
2.  Enter OpenRouter API Key\
3.  Ask questions from your notes\
4.  Get accurate AI‑generated answers

## 🤝 Contributing

Pull requests are welcome!\
For major changes, please open an issue first.

## 📜 License

MIT License
