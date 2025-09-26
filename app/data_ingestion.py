# app/data_ingestion.py

import pandas as pd
import requests

def load_data_from_csv(file_path: str) -> pd.DataFrame:
    """Reads customer data from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        print(f"[INFO] Loaded {len(df)} rows from {file_path}")
        return df
    except Exception as e:
        print(f"[ERROR] Failed to load CSV: {e}")
        return pd.DataFrame()

def load_data_from_api(api_url: str, headers: dict = None) -> pd.DataFrame:
    """Fetches customer data from an API endpoint."""
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame(data)
        print(f"[INFO] Loaded {len(df)} rows from API")
        return df
    except Exception as e:
        print(f"[ERROR] Failed to fetch API data: {e}")
        return pd.DataFrame()
