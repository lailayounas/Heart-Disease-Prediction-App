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

🔗 Run Locally
1️⃣ Clone Repository
git clone <your-repo-link>
cd Heart-Disease-Prediction-App
2️⃣ Create Virtual Environment
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run App
streamlit run app.py
🌐 Access URLs (After Running)
🖥 Local URL: http://localhost:8501
🌐 Network URL: http://192.168.10.14:8501
☁️ Hugging Face Deployment

This app is deployed on Hugging Face Spaces:

👉 https://huggingface.co/spaces/laila123younas/cardio-predictor

Steps:

Upload project files
Add requirements.txt
Hugging Face auto-builds app
Get public URL instantly
🐳 Docker Deployment (Optional)
docker build -t heart-disease-app .

docker run -p 8501:8501 heart-disease-app
📂 Project Structure
Heart-Disease-Prediction-App/
│
├── app.py
├── train_model.py
├── heart.csv
├── model.pkl
├── scaler.pkl
├── encoder.pkl
├── requirements.txt
├── Dockerfile
└── assets/
    ├── main_ui_screen.png
    └── main_two.png
⚙️ Tech Stack
Python 🐍
Streamlit 🌐
scikit-learn 🤖
Pandas & NumPy 📊
Docker 🐳
Hugging Face Spaces ☁️
✨ Features
Heart disease prediction using ML
Clean Streamlit UI
Real-time prediction
Preprocessing (Scaler + Encoder)
Cloud deployment ready
📜 License

This project is licensed under the MIT License.

⭐ Author

Built with ❤️ by You

✅ IMPORTANT (READ THIS)

✔ Save file as: README.md
✔ Do NOT wrap in ```
✔ Keep images inside: assets/
✔ Push again after update

If you want next level upgrade, I can:
🚀 
Make this look like a startup landing page README
🚀 
Add animated GIF preview
🚀 Or 
help you deploy it live step-by-step

Just tell me 👍```plaintext
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

