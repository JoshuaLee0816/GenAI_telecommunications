from rag.vector_store import VectorStore

def test_vector_store_basic():
    chunks = [
        {"title": "doc1", "chunk_id": 0, "content": "Hello world"},
        {"title": "doc2", "chunk_id": 1, "content": "I am a student"},
        {"title": "doc3", "chunk_id": 2, "content": "Life is so amazing"},
    ]

    store = VectorStore()
    store.build_index(chunks)

    results = store.query("Hello")
    assert len(results) > 0
    assert any("Hello" in r["content"] for r in results)