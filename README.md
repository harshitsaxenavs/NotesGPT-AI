
# NotesGPT-AI

**NotesGPT-AI** is a **Streamlit-based AI assistant** that allows you to upload PDF documents and ask questions about their content. It uses **LangChain**, **HuggingFace embeddings**, and **FAISS** for semantic search, and connects to the **OpenRouter API** for AI-powered answers.

This app is optimized for **speed, usability, and user experience**, featuring caching, dynamic relevance filtering, progress spinners, and expandable AI responses.  

**Explore your notes smarter with NotesGPT-AI!**

---
## 🟢 Live Demo

🔗 **Try it Live:** [Streamlit App](https://notesgpt-ai.streamlit.app/)  

---

## Features

- **PDF Upload & Processing**: Upload PDFs and extract text efficiently.  
- **Progress Feedback**: Real-time progress spinner during PDF processing and embedding creation.  
- **Chunking & Embeddings**: Splits PDF into meaningful chunks and creates embeddings using HuggingFace models.  
- **Vector Search**: Fast semantic search with FAISS.  
- **Dynamic Similarity Threshold**: Adjust relevance threshold with a slider to filter search results.  
- **Customizable Models**: Choose from multiple embedding models and LLMs.  
- **Interactive Queries**: Ask questions through a clean input interface.  
- **Expandable Answers**: AI responses appear in an expandable section for readability.  
- **Download Answers**: Save AI-generated answers as TXT files.  
- **Sidebar Info**: Displays PDF filename, size, number of pages, and model selections.  
- **Caching**: Embeddings are cached to speed up repeated queries.  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/NotesGPT-AI.git
cd NotesGPT-AI
```

2. Install dependencies:

```bash
pip install streamlit requests PyPDF2 langchain langchain-community faiss-cpu sentence-transformers
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
4. **Enter API Key**: Provide your OpenRouter API key for the selected model.  
5. **Set Relevance Threshold**: Use the slider to adjust the similarity threshold for filtering context.  
6. **Ask a Question**: Type your query and click the **Ask** button.  
7. **View Answer**: AI response appears in an expandable section.  
8. **Download Answer**: Click the download button to save the response as TXT.  
9. **Out-of-context Handling**: If your question is unrelated to the uploaded PDF, the app will display a **generic message**.  

---

## Recommended Embedding Models

- `sentence-transformers/all-MiniLM-L6-v2` – Fast, lightweight  
- `sentence-transformers/all-mpnet-base-v2` – Higher quality, slightly slower  
- `sentence-transformers/paraphrase-MiniLM-L3-v2` – Small and fast  

---

## Recommended AI Models

- `gpt-oss-20b` – Free-quality GPT OSS model  
- `google/gemini-2.0-flash-exp:free` – Google Gemini 2.0 Flash 

---

## UI/UX Improvements

- Spinner during PDF processing, chunking, and embedding creation.  
- Dynamic status messages for user feedback.  
- Expandable answer section for cleaner readability.  
- Sidebar with clear sections for PDF stats, embedding selection, and model selection.  
- Query button triggers API calls only when needed.  

---

## Future Improvements

- Multi-file upload and combined semantic search.  
- Highlighting relevant text in the PDF based on the AI answer.  
- Offline embeddings to avoid API calls.  
- Persistent API keys using session state.  
- Additional model support for more accurate answers.  

---

## License

MIT License  
Copyright (c) 2025 Harshit Saxena
