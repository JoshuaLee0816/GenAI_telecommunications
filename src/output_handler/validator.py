# src/output_handler/validator.py

from typing import Dict, Any, List

class ValidationError(Exception):
    pass

class OutputValidator:
    """
    Check LLM structured output against a predefined schema.
    """

    # questions: what if future fields are added?
    ALLOWED_CATEGORIES: List[str] = [
        "network_outage", "billing_issue", "equipment_repair", "other"
    ]

    ALLOWED_SEVERITIES: List[str] = [
        "low", "medium", "high", "critical"
    ]

    REQUIRED_FIELDS: List[str] = [
        "ticket_type",
        "severity",
        "escalation_required",
        "recommendation_actions",
        "confidence"
    ]

    def __init__(self, strict: bool = True):
        self.strict = strict
    
    def validate(self, output: Dict[str, Any]) -> Dict[str, Any]:
        errors = []

        for field in self.REQUIRED_FIELDS:
            if field not in output:
                errors.append(f"lacking required field: {field}")

        if errors:
            return self._handle_errors(errors, output)

