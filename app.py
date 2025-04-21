import streamlit as st
import joblib
import numpy as np

st.title("ML Predictor: A Divided by B")

# Load model
model = joblib.load("model.pkl")

# Inputs
a = st.number_input("Enter number A", value=1.0)
b = st.number_input("Enter number B", value=1.0)

# Prediction
if b != 0:
    ratio = a / b
    st.write(f"A / B = {ratio:.2f}")
    
    prediction = model.predict(np.array([[ratio]]))[0]
    label = "Positive" if prediction == 1 else "Negative"
    
    st.success(f"Prediction: {label}")
else:
    st.error("Division by zero is not allowed.")
