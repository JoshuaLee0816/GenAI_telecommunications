# src/output_handler/validator.py

from typing import Dict, Any, List

class ValidationError(Exception):
    pass

class OutputValidator:

    ALLOWED_CATEGORIES: List[str] = [
        "network_issue", "billing_issue", "equipment_issue"
    ]

    ALLOWED_PRIORITIES: List[str] = [
        "LOW", "MEDIUM", "HIGH"
    ]

    REQUIRED_FIELDS: List[str] = [
        "category",
        "priority",
        "recommended_action"
    ]

    def __init__(self, strict: bool = True):
        self.strict = strict

    def validate(self, output: Dict[str, Any]) -> Dict[str, Any]:
        errors = []

        for field in self.REQUIRED_FIELDS:
            if field not in output:
                errors.append(f"Missing required field: {field}")

        if "category" in output and output["category"] not in self.ALLOWED_CATEGORIES:
            errors.append(f"Invalid category: {output['category']}")

        if "priority" in output and output["priority"] not in self.ALLOWED_PRIORITIES:
            errors.append(f"Invalid priority: {output['priority']}")

        if "recommended_action" in output and not isinstance(output["recommended_action"], str):
            errors.append("recommended_action must be a string")

        if errors:
            if self.strict:
                raise ValidationError("; ".join(errors))
            else:
                output["_validation_errors"] = errors

        return output
