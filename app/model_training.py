# app/model_training.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
import joblib
import os

def train_credit_model(
    df: pd.DataFrame,
    feature_cols: list,
    target_col: str,
    model_path: str = "models/credit_model.pkl"
) -> None:
    """
    Trains a logistic regression model for credit scoring and saves it securely.

    Parameters:
        df (pd.DataFrame): Cleaned and preprocessed data.
        feature_cols (list): List of feature column names.
        target_col (str): Name of the target column.
        model_path (str): Path to save the trained model.

    Raises:
        ValueError: If required columns are missing or data is insufficient for secure training.
    """

    # بررسی وجود ستون‌ها
    required = feature_cols + [target_col]
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f"[SECURITY BLOCK] Missing required columns: {missing}")

    # بررسی تعداد کلاس‌ها برای آموزش امن
    y = df[target_col]
    class_counts = y.value_counts()
    if len(class_counts) < 2:
        raise ValueError("[SECURITY BLOCK] Target column must contain at least two classes.")
    if class_counts.min() < 2:
        raise ValueError(f"[SECURITY BLOCK] Class '{class_counts.idxmin()}' has only {class_counts.min()} sample(s). Minimum required is 2.")

    # جداسازی داده‌ها
    X = df[feature_cols]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # آموزش مدل
    model = LogisticRegression(
        max_iter=1000,
        class_weight='balanced',
        solver='liblinear'  # امن‌تر برای داده‌های کوچک و sparse
    )
    model.fit(X_train, y_train)

    # ارزیابی مدل
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]
    print("[INFO] Classification Report:")
    print(classification_report(y_test, y_pred))
    print(f"[INFO] ROC AUC Score: {roc_auc_score(y_test, y_proba):.4f}")

    # ذخیره امن مدل
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    print(f"[SUCCESS] Model securely saved to: {model_path}")