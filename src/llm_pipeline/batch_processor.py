# src/llm_pipeline/batch_processor.py

from typing import List, Dict, Any
from src.data_loader.models import Ticket
from src.llm_pipeline.analyzer import TicketAnalyzer

class BatchProcessor:
    def __init__(self, analyzer: TicketAnalyzer):
        self.analyzer = analyzer
    
    def process_tickets(self, tickets: List[Ticket]) -> List[Dict[str, Any]]:
        results = []
        for ticket in tickets:
            try:
                result = self.analyzer.analyze_ticket(ticket)
                results.append(result)
            except Exception as e:
                results.append({"ticket_id": ticket.ticket_id, "error": str(e)})
        return results
    