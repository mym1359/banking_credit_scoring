# run_training.py

from app.data_ingestion import load_data_from_csv
from app.preprocessing import clean_data, normalize_features, standardize_column_names
from app.model_training import train_credit_model

# مرحله ۱: بارگذاری داده‌ها
df = load_data_from_csv("data/sample.csv")

# مرحله ۲: اصلاح نام ستون‌ها و پاک‌سازی
df = standardize_column_names(df)
df_clean = clean_data(df)

# مرحله ۳: تعریف ویژگی‌ها و هدف
feature_cols = ["income", "credit_score"]
target_col = "target"  # باید در فایل CSV موجود باشه

# مرحله ۴: بررسی وجود ستون هدف
if target_col not in df_clean.columns:
    print(f"[ERROR] ستون هدف '{target_col}' در داده‌ها وجود ندارد.")
else:
    # مرحله ۵: نرمال‌سازی ویژگی‌ها
    df_clean = normalize_features(df_clean, feature_cols)

    # مرحله ۶: آموزش مدل
    train_credit_model(df_clean, feature_cols, target_col)
