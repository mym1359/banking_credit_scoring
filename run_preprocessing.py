# run_preprocessing.py

from app.data_ingestion import load_data_from_csv
from app.preprocessing import clean_data, normalize_features

# مرحله ۱: بارگذاری داده‌ها
df = load_data_from_csv("data/sample.csv")

# مرحله ۲: پاک‌سازی داده‌ها
df_clean = clean_data(df)

# مرحله ۳: چاپ ستون‌های موجود برای بررسی دقیق
print("[DEBUG] ستون‌های موجود پس از پاک‌سازی:")
for col in df_clean.columns:
    print(f"- '{col}'")

# مرحله ۴: اصلاح نام ستون‌ها برای جلوگیری از خطاهای KeyError
df_clean.columns = df_clean.columns.str.strip().str.lower()

# مرحله ۵: بررسی وجود ستون‌های مورد نیاز
required_cols = ["income", "credit_score"]
missing = [col for col in required_cols if col not in df_clean.columns]

if missing:
    print(f"[ERROR] ستون‌های مورد نیاز پیدا نشدند: {missing}")
else:
    # مرحله ۶: نرمال‌سازی ویژگی‌ها
    df_norm = normalize_features(df_clean, required_cols)
    print("[SUCCESS] داده‌ها نرمال‌سازی شدند:")
    print(df_norm.head())
