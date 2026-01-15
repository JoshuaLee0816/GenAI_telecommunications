# src/main.py

from typing import List
from data_loader.models import Ticket
from llm_pipeline.analyzer import TicketAnalyzer
from llm_pipeline.batch_processor import BatchProcessor

def load_tickets() -> List[Ticket]:
    """
    Temporary mock data loader.
    Later can be replaced with actuat data like CSV
    """
    return [
        Ticket(
            ticket_id=1,
            category="network_issue",
            description="Internet down at office",
            timestamp="2023-01-29 10:00:00"
        ),
        Ticket(
            ticket_id=2,
            category="billing_issue",
            description="Urgent billing discrepancy",
            timestamp="2024-12-14 11:19:00"
        )
    ]

def main():
    # Load tickets
    tickets = load_tickets()

    # Initialize analyzer
    analyzer = TicketAnalyzer(
        knowledge_base_path="data/knowledge_base"
    )
    batch_processor = BatchProcessor(analyzer)
    results = batch_processor.process_tickets(tickets)

    # Output results
    print("Batch processing results:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
