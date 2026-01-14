import pytest
from typing import Any, Dict, List
from data_loader.models import Ticket
from llm_pipeline.analyzer import TicketAnalyzer
from llm_pipeline.batch_processor import BatchProcessor

class DummyRetriever:
    def query(self, description, top_k=3):
        return "Relevant knowledge snippet"

class DummyAnalyzer(TicketAnalyzer):
    def __init__(self):
        self.retriever = DummyRetriever()
        self.llm_model = "dummy"  

    def analyze_ticket(self, ticket: Ticket) -> Dict[str, Any]:
        if ticket.description.strip() == "":
            raise ValueError("Description cannot be empty")
        if ticket.category not in ["network_issue", "billing_issue", "equipment_issue"]:
            raise ValueError("Invalid category")
        return {
            "ticket_id": ticket.ticket_id,
            "analysis": f"Processed {ticket.description}",
            "priority": "high" if "urgent" in ticket.description.lower() else "normal"
        }

@pytest.fixture
def batch_processor() -> BatchProcessor:
    analyzer = DummyAnalyzer()
    return BatchProcessor(analyzer)

def test_process_tickets_success(batch_processor: BatchProcessor):
    tickets: List[Ticket] = [
        Ticket(ticket_id=1, category="network_issue", description="Internet down", timestamp="2026-01-14 10:00:00"),
        Ticket(ticket_id=2, category="billing_issue", description="Billing error urgent", timestamp="2026-01-14 11:00:00")
    ]
    results = batch_processor.process_tickets(tickets)

    assert len(results) == 2
    assert results[0]["ticket_id"] == 1
    assert results[0]["priority"] == "normal"
    assert results[1]["ticket_id"] == 2
    assert results[1]["priority"] == "high"

def test_process_tickets_with_errors(batch_processor: BatchProcessor):
    tickets: List[Ticket] = [
        Ticket(ticket_id=1, category="network_issue", description="", timestamp="2026-01-14 10:00:00"),
        Ticket(ticket_id=2, category="invalid_category", description="Something wrong", timestamp="2026-01-14 11:00:00")
    ]
    results = batch_processor.process_tickets(tickets)

    assert len(results) == 2
    # First ticket fails due to empty description
    assert "error" in results[0]
    assert results[0]["ticket_id"] == 1
    assert "Description cannot be empty" in results[0]["error"]
    # Second ticket fails due to invalid category
    assert "error" in results[1]
    assert results[1]["ticket_id"] == 2
    assert "Invalid category" in results[1]["error"]
