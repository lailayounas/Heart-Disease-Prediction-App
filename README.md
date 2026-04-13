# ❤️ Heart Disease Prediction App

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-green?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Docker](https://img.shields.io/badge/Docker-Container-blue?logo=docker&logoColor=white)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## 🧠 Overview
The **Heart Disease Prediction App** is a machine learning web application that predicts the likelihood of heart disease based on medical and clinical parameters.

It uses a trained ML model and provides real-time predictions through a simple and interactive Streamlit interface.

---

## 🚀 Live Demo
Check the live app here: [Hugging Face Demo](https://huggingface.co/spaces/laila123younas/cardio-predictor)
## 📸 App Preview


<!-- PUT YOUR SCREENSHOTS HERE -->
![UI Screenshot 1](assets/main_ui_screen.png)
![UI Screenshot 2](assets/main_two.png)

---

## ✨ Features
- Predict heart disease risk using ML model
- User-friendly Streamlit interface
- Data preprocessing using scaler and encoder
- Trained model saved as `model.pkl`
- Easy to run locally or deploy using Docker

---

## 📂 Project Structure

```plaintext
Heart-Disease-Prediction-App/
│
├── app.py                # Main Streamlit app
├── train_model.py       # Model training script
├── heart.csv            # Dataset
├── model.pkl            # Trained ML model
├── scaler.pkl           # Feature scaling
├── encoder.pkl          # Label encoding
├── requirements.txt     # Dependencies
├── Dockerfile           # Docker setup
└── assets/              # Screenshots folder
    ├── main_ui_screen.png
    └── main_two.png
⚙️ Installation
1. Clone Repository
git clone https://github.com/lailayounas/Heart-Disease-Prediction-App.git
cd Heart-Disease-Prediction-App
2. Install Dependencies
pip install -r requirements.txt
3.Run Application
streamlit run app.py
Then open:
http://localhost:8501
🐳 Docker Deployment (Optional)
# Build Docker image
docker build -t heart-disease-app .
# Run container
docker run -p 8501:8501 heart-disease-app
🧪 Tech Stack
Python 🐍
Streamlit 🌐
scikit-learn 🤖
Pandas & NumPy 📊
Docker 🐳
🤝 Contributing
Contributions are welcome!
Fork the repo
Create a new branch
Commit changes
Push and create PR
Author:
Built with ❤️ by laila younas

