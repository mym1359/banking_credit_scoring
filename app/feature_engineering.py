# feature_engineering.py

import pandas as pd
import numpy as np
import logging
from sklearn.feature_selection import SelectKBest, f_classif

# Setup logging
logging.basicConfig(filename='logs/feature_engineering.log', level=logging.INFO)

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Starting feature engineering...")

    # Example: Debt-to-Income Ratio
    df['debt_to_income'] = df['debt'] / (df['income'] + 1e-6)
    logging.info("Created debt_to_income feature.")

    # Example: Age group
    df['age_group'] = pd.cut(df['age'], bins=[18, 30, 45, 60, 100], labels=['18-30', '31-45', '46-60', '60+'])
    logging.info("Created age_group feature.")

    # Example: Employment stability
    df['employment_stability'] = df['employment_years'] / df['age']
    logging.info("Created employment_stability feature.")

    # Drop irrelevant or sensitive columns
    drop_cols = ['customer_id', 'name', 'ssn']
    df = df.drop(columns=[col for col in drop_cols if col in df.columns], errors='ignore')
    logging.info(f"Dropped columns: {drop_cols}")

    logging.info("Feature engineering completed.")
    return df

def select_best_features(X: pd.DataFrame, y: pd.Series, k: int = 10) -> pd.DataFrame:
    logging.info(f"Selecting top {k} features using ANOVA F-test...")
    selector = SelectKBest(score_func=f_classif, k=k)
    X_new = selector.fit_transform(X, y)
    selected_features = X.columns[selector.get_support()]
    logging.info(f"Selected features: {list(selected_features)}")
    return pd.DataFrame(X_new, columns=selected_features)
