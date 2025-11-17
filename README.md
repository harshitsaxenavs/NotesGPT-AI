
# NotesGPT-AI

NotesGPT-AI is a **Streamlit-based AI chatbot** that allows you to upload PDF documents and ask questions about their content. It uses **LangChain**, **HuggingFace embeddings**, and **FAISS** for semantic search, and connects to the **OpenRouter API** for AI-powered answers.  

This app is optimized for **speed, UX, and usability**, featuring progress bars, status messages, and expandable answers.  

**Enjoy smarter PDF notes exploration with NotesGPT-AI!**

---

## Features

- **PDF Upload & Processing**: Upload PDFs and extract text efficiently.  
- **Progress Feedback**: Real-time progress bar while processing PDF pages.  
- **Chunking & Embeddings**: Splits PDF into chunks for meaningful context and creates embeddings using HuggingFace models.  
- **Vector Search**: Fast semantic search using FAISS.  
- **Customizable Models**: Choose from different embedding models and LLMs.  
- **Interactive Queries**: Ask questions via a clean interface with a button-triggered query.  
- **Expandable Answers**: AI responses appear in an expandable section.  
- **Download Answers**: Easily download the AI-generated answer as a TXT file.  
- **Sidebar Info**: View PDF stats (filename, size, pages) and manage model selections.  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/NotesGPT-AI.git
cd NotesGPT-AI
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app.py
```

---

## Usage

1. **Upload PDF**: Use the sidebar to upload your PDF file.  
2. **View PDF info**: File name, size, and number of pages are displayed in the sidebar.  
3. **Select Models**: Choose the embedding model and AI model for query processing.  
4. **Enter API Key**: Provide your OpenRouter API key.  
5. **Ask a Question**: Type your query and click the **Ask** button.  
6. **View Answer**: The AI response appears in an expandable section.  
7. **Download Answer**: Click the download button to save the answer.  

---

## Recommended Embedding Models

- `sentence-transformers/all-MiniLM-L6-v2` – Fast, lightweight  
- `sentence-transformers/all-mpnet-base-v2` – Higher quality, slightly slower  
- `sentence-transformers/paraphrase-MiniLM-L3-v2` – Small & fast for simple queries  

---

## Recommended AI Models

- `gpt-oss-20b` – Free-quality GPT OSS model  
- `google/gemini-2.0-flash-exp:free` – Google Gemini 2.0 Flash  

---

## UI/UX Improvements

- Progress bar during PDF processing for real-time feedback.  
- Dynamic status messages for extraction, chunking, and embedding creation.  
- Expandable answer section for readability.  
- Sidebar with clear sections for PDF info, embeddings, and model selection.  
- Button-triggered queries to avoid unnecessary API calls.  

---


## Future Improvements

- Multi-file upload and combined search.  
- Caching embeddings for faster repeated processing.  
- Offline embeddings to avoid API calls.  
- Semantic highlighting of answers in the PDF.  
- Storing API key in session state for convenience.  

---

## License

MIT License
Copyright (c) 2025 Harshit Saxena

---


