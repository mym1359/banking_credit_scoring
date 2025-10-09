# model_training.py

import pandas as pd
import logging
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
import joblib
import os

# Setup logging
logging.basicConfig(filename='logs/model_training.log', level=logging.INFO)

def train_model(df: pd.DataFrame, target_column: str = 'default') -> None:
    logging.info("Starting model training...")

    # Split features and target
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    logging.info(f"Data split: {len(X_train)} train, {len(X_test)} test")

    # Model and hyperparameter tuning
    model = RandomForestClassifier(random_state=42)
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [5, 10, None],
        'min_samples_split': [2, 5]
    }

    grid_search = GridSearchCV(model, param_grid, cv=5, scoring='roc_auc', n_jobs=-1)
    grid_search.fit(X_train, y_train)
    best_model = grid_search.best_estimator_
    logging.info(f"Best parameters: {grid_search.best_params_}")

    # Evaluation
    y_pred = best_model.predict(X_test)
    auc = roc_auc_score(y_test, best_model.predict_proba(X_test)[:, 1])
    logging.info(f"AUC Score: {auc}")
    logging.info("Classification Report:\n" + classification_report(y_test, y_pred))

    # Save model securely
    os.makedirs('models', exist_ok=True)
    joblib.dump(best_model, 'models/credit_model.pkl')
    logging.info("Model saved to models/credit_model.pkl")
