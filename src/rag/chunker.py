# src/rag/chunker.py

from typing import List, Dict

class Chunker:
    def __init__(self, chunk_size: int = 200, overlap: int = 40):
        self.chunk_size = chunk_size
        self.overlap = overlap
    
    def chunk_document(self, doc: Dict) -> List[Dict]:
        text = doc["content"]
        chunks = []
        start = 0
        chunk_id = 0
        while start < len(text):
            end = min(start + self.chunk_size, len(text))
            chunk_text = text[start:end]
            chunks.append({
                "title":doc["title"],
                "chunk_id":chunk_id,
                "content":chunk_text
            })
            start += self.chunk_size - self.overlap
            chunk_id += 1
        return chunks
    
    def chunk_documents(self, documents: List[Dict]) -> List[Dict]:
        all_chunks = []
        for doc in documents:
            all_chunks.extend(self.chunk_document(doc))
        return all_chunks