from rag.chunker import Chunker

def test_chunker_basic():
    doc = {"title": "test_doc", "content": "0123456789"*50} # 500letters
    chunker = Chunker(chunk_size = 100, overlap = 20)
    chunks = chunker.chunk_document(doc)

    assert len(chunks) > 0
    assert all("title" in c and "chunk_id" in c and "content" in c for c in chunks)
    assert chunks[0]["content"][:10] == "0123456789"

