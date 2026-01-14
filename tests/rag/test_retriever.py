# tests/rag/test_retriever.py

from rag.retriever import Retriever


class FakeVectorStore:
    def query(self, query, top_k):
        return [
            {
                "content": "Network issue troubleshooting steps",
                "title": "network_guide",
                "score": 0.92
            }
        ]


def test_retriever_returns_context():
    store = FakeVectorStore()
    retriever = Retriever(store)

    results = retriever.retrieve("network issue", top_k=3)

    assert len(results) == 1
    assert "content" in results[0]
    assert "source" in results[0]
    assert results[0]["source"] == "network_guide"
