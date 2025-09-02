from qdrant_client import QdrantClient
from qdrant_client.http import models
from sentence_transformers import SentenceTransformer
from app.config import QDRANT_URL, QDRANT_COLLECTION, EMBEDDING_MODEL

# Embedding model
embedding_model = SentenceTransformer(EMBEDDING_MODEL)

# Qdrant client
qdrant = QdrantClient(QDRANT_URL)

def create_collection():
    """Ensure Qdrant collection exists."""
    qdrant.recreate_collection(
        collection_name=QDRANT_COLLECTION,
        vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE),
    )

def insert_document(text: str, doc_id: int):
    """Insert document chunk into Qdrant."""
    vector = embedding_model.encode(text).tolist()
    qdrant.upsert(
        collection_name=QDRANT_COLLECTION,
        points=[models.PointStruct(id=doc_id, vector=vector, payload={"text": text})]
    )

def search_query(query: str, top_k=3):
    """Retrieve top_k relevant chunks from Qdrant."""
    vector = embedding_model.encode(query).tolist()
    hits = qdrant.search(
        collection_name=QDRANT_COLLECTION,
        query_vector=vector,
        limit=top_k
    )
    return [hit.payload["text"] for hit in hits]
