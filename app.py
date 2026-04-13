import streamlit as st
import pandas as pd
import numpy as np
import joblib

# --- Load saved objects (ONLY joblib) ---
model = joblib.load("model.pkl")
encoder = joblib.load("encoder.pkl")
scaler = joblib.load("scaler.pkl")

# --- Streamlit App ---
st.set_page_config(page_title="Heart Disease Prediction", layout="centered")
st.title("❤️ Heart Disease Prediction App")
st.write("Enter patient details to predict the risk of heart disease:")

# --- Input Fields ---
age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type", ["Typical", "Atypical", "Non-anginal", "Asymptomatic"])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", value=120)
chol = st.number_input("Serum Cholesterol (mg/dl)", value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl?", ["Yes", "No"])
restecg = st.selectbox("Resting ECG", ["Normal", "ST-T abnormality", "Left ventricular hypertrophy"])
thalach = st.number_input("Max Heart Rate Achieved", value=150)
exang = st.selectbox("Exercise Induced Angina?", ["Yes", "No"])
oldpeak = st.number_input("ST Depression (Oldpeak)", value=1.0)
slope = st.selectbox("Slope of Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
ca = st.number_input("Major Vessels Colored by Fluoroscopy (0-3)", min_value=0, max_value=3, value=0)
thal = st.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])

# --- Predict Button ---
if st.button("Predict"):
    
    # --- Create DataFrame ---
    input_df = pd.DataFrame({
        "age":[age],
        "trestbps":[trestbps],
        "chol":[chol],
        "thalach":[thalach],
        "oldpeak":[oldpeak],
        "sex":[sex],
        "cp":[cp],
        "fbs":[fbs],
        "restecg":[restecg],
        "exang":[exang],
        "slope":[slope],
        "ca":[ca],
        "thal":[thal]
    })

    # --- Encode categorical columns ---
    cat_cols = ["sex","cp","fbs","restecg","exang","slope","ca","thal"]
    encoded_cat = encoder.transform(input_df[cat_cols])
    encoded_cat_df = pd.DataFrame(
        encoded_cat,
        columns=encoder.get_feature_names_out(cat_cols)
    )

    # --- Scale numeric columns ---
    num_cols = ["age","trestbps","chol","thalach","oldpeak"]
    input_df[num_cols] = scaler.transform(input_df[num_cols])

    # --- Final input ---
    final_input = pd.concat([input_df[num_cols], encoded_cat_df], axis=1)

    # --- Prediction ---
    prediction = model.predict(final_input)[0]

    if prediction == 1:
        st.error("High risk of heart disease ❌")
    else:
        st.success("Low risk of heart disease ✅")