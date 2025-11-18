import streamlit as st
import requests
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

st.header("NotesGPT-AI")

# ----- Sidebar -----
with st.sidebar:
    st.title("My Notes")
    with st.spinner("Processing PDF..."):
        file = st.file_uploader("Upload your PDF file:",type="pdf")


# ----- Extract PDF -----
if file is not None:
    with st.spinner("Processing PDF..."):
        st.sidebar.write(f"**Filename:** {file.name}")
        st.sidebar.write(f"**File size:** {round(file.size / 1024, 2)} KB")
        pdf = PdfReader(file)
        # Extract text from all pages
        text = "\n".join([page.extract_text() or "" for page in pdf.pages])
        if text is not None:
            st.success("PDF processed successfully!")
        else:
            st.error("PDF failed to process")
        # ----- Split into chunks -----
        splitter = RecursiveCharacterTextSplitter(
            separators=["\n\n", "\n", ".", "!", "?"],
            chunk_size=300,
            chunk_overlap=50,
            length_function=len
        )

        #with st.spinner("Splitting PDF into chunks..."):
            #status = st.empty()
        chunks = splitter.split_text(text)
           # status.text("Chunks ready!")



        chunks = [c for c in chunks if c.strip()]

    # ----- EMBEDDING MODEL SELECTION -----
    st.subheader("Choose Embedding Model")
    embedding_choice = st.selectbox(
        "Select embedding model:",
        [
            "sentence-transformers/all-MiniLM-L6-v2",  # Faster, smaller
            "sentence-transformers/all-mpnet-base-v2",  # Better quality, slightly slower
            "sentence-transformers/paraphrase-MiniLM-L3-v2"
        ]
    )
    # ----- Initialize Embeddings -----
    #status.text("Creating embeddings...")
    #embeddings = HuggingFaceEmbeddings(model_name=embedding_choice)
    # #status.success("Embeddings ready!")

    # Create FAISS vector store
    #vector_store = FAISS.from_texts(chunks, embeddings)
    @st.cache_data
    def get_vector_store(chunks, embedding_choice):
        embeddings = HuggingFaceEmbeddings(model_name=embedding_choice)
        return FAISS.from_texts(chunks, embeddings)


    vector_store = get_vector_store(chunks, embedding_choice)

    # ----- MODEL SELECTION -----
    st.subheader("Choose Model")
    model_choice = st.selectbox(
        "Select model:",
        [
            "gpt-oss-20b",                 # Free-quality GPT OSS model
            "google/gemini-2.0-flash-exp:free",  # Gemini 2.0 Flash
        ]
    )



    # ----- OpenRouter API Key -----
    api_key1 = ""
    api_key2 = ""
    if model_choice == "gpt-oss-20b":
        st.subheader("Enter your GPT API Key")
        api_key1 = st.text_input("API Key", type="password")
    else:
        st.subheader("Enter your Gemini API Key")
        api_key2 = st.text_input("API Key", type="password")


    api_key = api_key1 if model_choice == "gpt-oss-20b" else api_key2



    # ----- Query -----

    if api_key:
        query = st.text_input("Ask something from your uploaded notes:")
        relevant_threshold = st.slider("Relevance threshold", 0.0, 1.0, 0.5)
        if st.button("Ask") and query.strip():


            with st.spinner("Fetching answer..."):

                # Vector search with scores
                docs_with_scores = vector_store.similarity_search_with_score(query, k=10)

                # Filter docs with a reasonable similarity threshold (e.g., 0.5)
                threshold = relevant_threshold

                relevant_docs = [d for d, score in docs_with_scores if score >= threshold]

                if not relevant_docs:
                    st.info("Sorry, I can only answer questions related to your uploaded notes.")
                else:
                    context = "\n".join([d.page_content for d in relevant_docs])
                    # Final prompt
                    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
                    # ... proceed with API request

                # ───── OpenRouter Request ─────
                url = "https://openrouter.ai/api/v1/chat/completions"
                headers = {
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                }

                data = {
                    "model": model_choice,
                    "messages": [
                        {"role": "user", "content": prompt}
                    ]
                }

                try:
                    response = requests.post(url, headers=headers, json=data).json()
                    if "choices" in response:
                        answer = response["choices"][0]["message"]["content"]
                        st.write(answer)
                        st.download_button("Download Answer", answer, file_name="answer.txt")
                        st.balloons()
                    else:
                        st.error("API Error:\n" + str(response))
                except Exception as e:
                    st.error(f"Error fetching response: {e}")
    else:
        st.warning("Please enter a valid API Key for the selected model.")