# 🏦 Banking Credit Scoring System

A secure, scalable machine learning system for assessing credit risk in banking. Designed with modular architecture, automated pipelines, and RESTful API deployment. Built for real-world use and global talent recognition.

---

## 📊 Features

- ✅ Secure data preprocessing with input validation
- ✅ Feature engineering with statistical selection
- ✅ Model training with GridSearchCV and AUC optimization
- ✅ REST API with FastAPI for real-time scoring
- ✅ Dockerized deployment and CI/CD integration
- ✅ Bilingual documentation (English & Persian)

---

## 📁 Project Structure
banking_credit_scoring/
├── preprocessing.py
├── feature_engineering.py
├── model_training.py
├── api.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── README.fa.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── models/
├── logs/ └── data/


---

## 🚀 Installation & Execution

```bash
# Clone the repo
git clone https://github.com/mym1359/banking_credit_scoring.git
cd banking_credit_scoring

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run model training
python model_training.py

# Run API
uvicorn api:app --reload

🐳 Docker Deployment
# Build and run with Docker Compose
docker-compose up --build


Access the API at: http://localhost:8000/docs

🔌 API Endpoint
POST /predict
Request Body:
{
  "income": 50000,
  "credit_score": 680,
  "debt": 12000,
  "age": 35,
  "employment_years": 7
}


Response:
{
  "risk_class": 1,
  "risk_probability": 0.8421
}




🌍 Bilingual Support
🔸 نسخه فارسی README

👨‍💻 Developer
- GitHub: mym1359
- Email: mym1359@gmail.com
- Location: Iran (Global Talent Applicant)

📜 License
This project is licensed under the MIT License.

🧭 Migration & Global Talent
This project is part of a professional portfolio for:
- 🇺🇸 National Interest Waiver (NIW – USA)
- 🇦🇺 Global Talent Visa (NIV – Australia)
It demonstrates secure, scalable, and documented credit scoring systems for financial institutions. The project includes daily GitHub activity, bilingual documentation, and full automation—proving global technical talent in FinTech and AI.


