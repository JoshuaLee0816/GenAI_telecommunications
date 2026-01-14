# src/rag/retriever.py

from typing import List, Dict
from .vector_store import VectorStore


class Retriever:
    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store

    def retrieve(self, query: str, top_k: int = 5) -> List[Dict]:
        """
        Retrieve top-k relevant document chunks for a query.
        """
        results = self.vector_store.query(query, top_k)

        retrieved = []
        for r in results:
            retrieved.append({
                "content": r["content"],
                "source": r.get("title", "unknown"),
                "score": r.get("score", None),
            })

        return retrieved
