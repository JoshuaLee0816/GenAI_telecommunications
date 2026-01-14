from rag.document_loader import DocumentLoader

def test_load_documents():
    loader = DocumentLoader()
    docs = loader.load_documents()
    assert isinstance(docs, list)
    assert all("title" in d and "content" in d for d in docs)
    assert len(docs) > 0
    