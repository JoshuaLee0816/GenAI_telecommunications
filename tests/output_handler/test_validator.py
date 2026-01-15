import pytest
from output_handler.validator import OutputValidator, ValidationError


@pytest.fixture
def strict_validator():
    return OutputValidator(strict=True)

@pytest.fixture
def loose_validator():
    return OutputValidator(strict=False)


# Test case
def test_validate_success(strict_validator):
    """
    Test Case: All fields are present and values are valid.
    Expected: The validator returns the input dictionary without modification.
    """
    data = {
        "category": "network_issue",
        "priority": "HIGH",
        "recommended_action": "Check the fiber optic cable."
    }
    result = strict_validator.validate(data)
    assert result == data
    assert "_validation_errors" not in result


def test_strict_missing_field(strict_validator):
    """
    Test Case: A required field ('priority') is missing.
    Expected: Raises ValidationError.
    """
    incomplete_data = {
        "category": "billing_issue",
        "recommended_action": "Refund the customer."
    }

    with pytest.raises(ValidationError) as excinfo:
        strict_validator.validate(incomplete_data)
    
    assert "Missing required field: priority" in str(excinfo.value)


def test_strict_invalid_enum_values(strict_validator):
    """
    Test Case: Category and Priority contain values not in the allowed lists.
    Expected: Raises ValidationError with both error messages.
    """
    bad_data = {
        "category": "unknown_type", 
        "priority": "URGENT",  # Should be HIGH/MEDIUM/LOW
        "recommended_action": "None"
    }
    with pytest.raises(ValidationError) as excinfo:
        strict_validator.validate(bad_data)
    
    error_msg = str(excinfo.value)
    assert "Invalid category" in error_msg
    assert "Invalid priority" in error_msg


def test_loose_mode_error_collection(loose_validator):
    """
    Test Case: Multiple errors occur in non-strict mode.
    Expected: No exception is raised; errors are stored in '_validation_errors'.
    """
    bad_data = {
        "category": "wrong",
        "priority": "MEDIUM"
        # Missing recommended_action
    }
    result = loose_validator.validate(bad_data)
    
    # In loose mode, the dictionary is returned with an extra key
    assert "_validation_errors" in result
    assert len(result["_validation_errors"]) == 2
    assert "Invalid category: wrong" in result["_validation_errors"]


def test_invalid_type_recommended_action(strict_validator):
    """
    Test Case: recommended_action is a list instead of a string.
    Expected: Raises ValidationError regarding type mismatch.
    """
    data = {
        "category": "equipment_issue",
        "priority": "LOW",
        "recommended_action": ["Step 1", "Step 2"] # Should be a string
    }
    with pytest.raises(ValidationError) as excinfo:
        strict_validator.validate(data)
    
    assert "recommended_action must be a string" in str(excinfo.value)