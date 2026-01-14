# src/data_loader/validator.py

import pandas as pd
from datetime import datetime

REQUIRED_COLUMNS = ["ticket_id", "category", "description", "timestamp"]
CATEGORY_OPTIONS = ["network_issue", "billing_issue", "equipment_issue"]

class DataValidator:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.errors = []

    def validate_columns(self):
        for col in REQUIRED_COLUMNS:
            if col not in self.df.columns:
                self.errors.append(f"Missing column: {col}")

    def validate_types(self):
        if "ticket_id" in self.df.columns:
            if not pd.api.types.is_integer_dtype(self.df["ticket_id"]):
                self.errors.append("ticket_id must be an integer")
        if "timestamp" in self.df.columns:
            try:
                pd.to_datetime(self.df["timestamp"])
            except Exception:
                self.errors.append("timestamp column has invalid format")

    def validate_categories(self):
        if "category" in self.df.columns:
            invalid = self.df[~self.df["category"].isin(CATEGORY_OPTIONS)]
            if not invalid.empty:
                self.errors.append(f"Invalid category found: {invalid['category'].unique()}")

    def validate_non_empty(self):
        for col in ["description"]:
            if col in self.df.columns:
                empty_rows = self.df[self.df[col].isnull() | (self.df[col].str.strip() == "")]
                if not empty_rows.empty:
                    self.errors.append(f"{col} column has empty values: {len(empty_rows)} rows")

    def validate_duplicates(self):
        if "ticket_id" in self.df.columns:
            duplicates = self.df[self.df.duplicated("ticket_id")]
            if not duplicates.empty:
                self.errors.append(f"Duplicate ticket_id found: {duplicates['ticket_id'].tolist()}")

    def validate_all(self):
        self.validate_columns()
        self.validate_types()
        self.validate_categories()
        self.validate_non_empty()
        self.validate_duplicates()
        return self.errors