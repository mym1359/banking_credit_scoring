# app/preprocessing.py

import pandas as pd
from sklearn.preprocessing import StandardScaler

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes missing values and duplicate rows from the DataFrame.

    Parameters:
        df (pd.DataFrame): Raw input data.

    Returns:
        pd.DataFrame: Cleaned data.
    """
    initial_rows = len(df)
    df = df.dropna()
    df = df.drop_duplicates()
    final_rows = len(df)
    print(f"[INFO] Cleaned data: {initial_rows} → {final_rows} rows")
    return df


def normalize_features(df: pd.DataFrame, feature_cols: list) -> pd.DataFrame:
    """
    Normalizes selected numerical features using StandardScaler.

    Parameters:
        df (pd.DataFrame): Input DataFrame.
        feature_cols (list): List of column names to normalize.

    Returns:
        pd.DataFrame: DataFrame with normalized features.

    Raises:
        ValueError: If any of the specified columns are missing.
    """
    missing = [col for col in feature_cols if col not in df.columns]
    if missing:
        raise ValueError(f"[ERROR] Missing columns for normalization: {missing}")

    scaler = StandardScaler()
    df[feature_cols] = scaler.fit_transform(df[feature_cols])
    print(f"[INFO] Normalized features: {feature_cols}")
    return df


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Strips whitespace and converts column names to lowercase.

    Parameters:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: DataFrame with standardized column names.
    """
    df.columns = df.columns.str.strip().str.lower()
    print("[INFO] Standardized column names")
    return df


if __name__ == "__main__":
    from app.data_ingestion import load_data_from_csv

    df = load_data_from_csv("data/sample.csv")
    df = standardize_column_names(df)
    df_clean = clean_data(df)

    try:
        df_norm = normalize_features(df_clean, ["income", "credit_score"])
        print("[SUCCESS] Normalized Data:")
        print(df_norm.head())
    except ValueError as e:
        print(e)