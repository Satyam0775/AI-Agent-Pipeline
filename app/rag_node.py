from langchain.text_splitter import RecursiveCharacterTextSplitter
from pypdf import PdfReader
from app.vectorstore import insert_document, search_query, create_collection

def load_pdf(pdf_path: str):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)

    create_collection()
    for i, chunk in enumerate(chunks):
        insert_document(chunk, i)

def rag_answer(query: str) -> str:
    """Return answer from stored PDF embeddings."""
    try:
        docs = search_query(query)
        return " ".join(docs) if docs else "No relevant information found."
    except Exception:
        return "No relevant information found."
