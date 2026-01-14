# src/rag/vector_store.py

from typing import List, Dict
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer   

class VectorStore:
    def __init__(self, embedding_model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(embedding_model_name)
        self.index = None
        self.metadata = []

    def build_index(self, chunks: List[Dict]):
        embeddings = [self.model.encode(c["content"]) for c in chunks]
        embeddings = np.array(embeddings).astype("float32")

        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)   #type: ignore

        self.metadata = chunks

    def query(self, text:str, top_k: int = 3) -> List[Dict]:
        if self.index is None:
            raise ValueError("Index is not built yet")
        query_vector = np.array([self.model.encode(text)]).astype("float32")
        D, I = self.index.search(query_vector, top_k)   #type: ignore
        results = [self.metadata[i] for i in I[0]]
        return results  