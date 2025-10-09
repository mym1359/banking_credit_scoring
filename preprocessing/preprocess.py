import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocesses the input DataFrame:
    - Drops duplicate rows
    - Fills missing numeric values with median
    - Fills missing categorical values with mode
    - Applies standard scaling to numeric features

    Args:
        df (pd.DataFrame): Raw input data

    Returns:
        pd.DataFrame: Cleaned and normalized data
    """
    # Drop duplicates
    df = df.drop_duplicates()

    # Separate numeric and categorical columns
    numeric_cols = df.select_dtypes(include='number').columns
    categorical_cols = df.select_dtypes(include='object').columns

    # Fill missing values
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Normalize numeric features
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df
