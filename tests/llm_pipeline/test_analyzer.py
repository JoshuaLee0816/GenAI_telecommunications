import pytest
from data_loader.models import Ticket
from llm_pipeline.analyzer import TicketAnalyzer

class DummyRetriever:
    def query(self, description, top_k=3):
        return "Relevant knowledge snippet"

class DummyAnalyzer(TicketAnalyzer):
    def __init__(self):
        self.retriever = DummyRetriever()
        self.llm_model = "dummy"

    def _validate_ticket(self, ticket):
        pass

    def _query_llm(self, prompt: str) -> str:
        return '{"category": "network_issue", "priority": "HIGH", "recommended_action": "Restart the router."}'
    
def test_analyze_success():
    analyzer = DummyAnalyzer()
    ticket = Ticket(
        ticket_id=1,
        category="network_issue",
        description="INternet is down",
        timestamp="2025-02-23 12:00:08"
    )

    result = analyzer.analyze_ticket(ticket)

    assert isinstance(result,dict)
    assert result["category"] == "network_issue"
    assert result["priority"] == "HIGH"
    assert result["recommended_action"] == "Restart the router."
