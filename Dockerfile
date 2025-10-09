# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Create logs and models folders if not exist
RUN mkdir -p logs models

# Default command to run model training
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
