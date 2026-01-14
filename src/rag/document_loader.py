# src/rag/document_loader.py

import os

class DocumentLoader:
    def __init__(self, kb_path="data/knowledge_base"):
        self.kb_path = kb_path
    
    def load_documents(self):
        documents = []
        for filename in os.listdir(self.kb_path):
            if filename.endswith(".md"):
                path = os.path.join(self.kb_path, filename)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                documents.append({
                    "title": filename.replace(".md", ""),
                    "content": content
                })
        return documents