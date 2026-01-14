import pytest
from data_loader.csv_reader import CSVReader

def test_load_csv():
    reader = CSVReader()
    df = reader.load()

    expected_columns = reader.expected_columns
    assert all(col in df.columns for col in expected_columns)

    assert len(df) > 0