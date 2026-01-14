import pandas as pd
import pytest
from data_loader.validator import DataValidator

# 建立一個正確範例 DataFrame
@pytest.fixture
def valid_df():
    return pd.DataFrame([
        {"ticket_id": 1, "category": "network_issue", "description": "Network down", "timestamp": "2026-01-14 10:00:00"},
        {"ticket_id": 2, "category": "billing_issue", "description": "Wrong bill", "timestamp": "2026-01-14 11:00:00"},
        {"ticket_id": 3, "category": "equipment_issue", "description": "Broken router", "timestamp": "2026-01-14 12:00:00"},
    ])

def test_valid_data(valid_df):
    validator = DataValidator(valid_df)
    errors = validator.validate_all()
    assert errors == []

def test_missing_column(valid_df):
    df = valid_df.drop(columns=["category"])
    validator = DataValidator(df)
    errors = validator.validate_all()
    assert "Missing column: category" in errors

def test_invalid_category(valid_df):
    df = valid_df.copy()
    df.at[0, "category"] = "invalid_category"
    validator = DataValidator(df)
    errors = validator.validate_all()
    assert any("Invalid category found" in e for e in errors)

def test_empty_description(valid_df):
    df = valid_df.copy()
    df.at[1, "description"] = ""
    validator = DataValidator(df)
    errors = validator.validate_all()
    assert any("description column has empty values" in e for e in errors)

def test_duplicate_ticket_id(valid_df):
    new_row = pd.DataFrame([{
        "ticket_id": 1,
        "category": "network_issue",
        "description": "Duplicate",
        "timestamp": "2026-01-14 13:00:00"
    }])
    df = pd.concat([valid_df, new_row], ignore_index=True)
    validator = DataValidator(df)
    errors = validator.validate_all()
    assert any("Duplicate ticket_id found" in e for e in errors)

def test_invalid_timestamp(valid_df):
    df = valid_df.copy()
    df.at[0, "timestamp"] = "not-a-date"
    validator = DataValidator(df)
    errors = validator.validate_all()
    assert "timestamp column has invalid format" in errors
