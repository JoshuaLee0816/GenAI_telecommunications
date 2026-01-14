from pathlib import Path
import pandas as pd

# csv_raw path
DATA_RAW_PATH = Path("data/raw/mock_tickets.csv")

class CSVReader:
    
    def __init__(self, csv_path = DATA_RAW_PATH):
        self.csv_path = csv_path
        self.expected_columns = [
            "ticket_id",
            "created_at",
            "issue_summary",
            "issue_description",
            "service_type",
            "affected_area",
            "device_type",
            "network_type",
            "outage_flag",
            "historical_ticket_count",
            "priority_hint"
        ]
    
    def load(self):
        df = pd.read_csv(self.csv_path)
        missing = set(self.expected_columns) - set(df.columns)
        if missing:
            raise ValueError(f"Missing columns in CSV: {missing}")
        return df
    
if __name__ == "__main__":
    reader = CSVReader()
    data = reader.load()
    print(data.head())
