# tests/test_preprocessing.py

import pandas as pd
from preprocessing.preprocess import preprocess

def test_preprocess_valid_data():
    df = pd.DataFrame({
        'age': [30, 45],
        'income': [50000, 70000],
        'credit_score': [650, 720],
        'debt': [10000, 15000],
        'employment_years': [5, 10]
    })
    processed = preprocess(df)
    assert processed.shape[0] == 2
    assert 'debt' in processed.columns
