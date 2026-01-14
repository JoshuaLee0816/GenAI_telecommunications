import pytest
from datetime import datetime
from pydantic import ValidationError
from data_loader.models import Ticket

def test_ticket_empty_description():
    with pytest.raises(ValidationError, match="Description cannot be empty"):
        Ticket(
            ticket_id=2,
            category="billing_issue",
            description="   ",
            timestamp="2026-01-14 11:00:00"
        )

def test_ticket_invalid_category():
    with pytest.raises(ValidationError, match="Input should be 'network_issue', 'billing_issue' or 'equipment_issue'"):
        Ticket(
            ticket_id=3,
            category="invalid_category",
            description="Some issue",
            timestamp="2026-01-14 12:00:00"
        )

def test_ticket_invalid_timestamp():
    with pytest.raises(ValidationError, match="Input should be a valid datetime or date"):
        Ticket(
            ticket_id=4,
            category="equipment_issue",
            description="Router broken",
            timestamp="not-a-date"
        )
