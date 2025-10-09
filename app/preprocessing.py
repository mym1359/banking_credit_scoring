# preprocessing.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from pydantic import BaseModel, ValidationError
import logging

# Setup logging
logging.basicConfig(filename='logs/preprocessing.log', level=logging.INFO)

# Input schema validation

class CustomerRecord(BaseModel):
    age: int
    income: float
    credit_score: float
    debt: float
    employment_years: int

def validate_row(row):
    try:
        CustomerRecord(**row)
        return True
    except ValidationError as e:
        logging.warning(f"Invalid row: {row} | Error: {e}")
        return False

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Starting preprocessing...")

    # Drop duplicates
    df = df.drop_duplicates()
    logging.info(f"Removed duplicates. Remaining rows: {len(df)}")

    # Validate rows
    df = df[df.apply(validate_row, axis=1)]
    logging.info(f"Validated rows. Remaining rows: {len(df)}")

    # Handle missing values
    df = df.fillna(df.median(numeric_only=True))
    logging.info("Filled missing values with median.")

    # Feature scaling
    scaler = StandardScaler()
    numeric_cols = ['income', 'credit_score', 'debt']
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    logging.info("Scaled numeric features.")

    logging.info("Preprocessing completed.")
    return df
