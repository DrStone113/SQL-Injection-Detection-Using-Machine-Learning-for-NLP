# app.py
# This script creates a Streamlit web application that loads a pre-trained model
# from the 'model' directory to detect SQL injection attacks in real-time.

import streamlit as st
import joblib
import re
from nltk.corpus import stopwords
import nltk
import os

# --- Define Paths ---
MODEL_PATH = 'model/model.pkl'
VECTORIZER_PATH = 'model/vectorizer.pkl'

# --- Load Model and Vectorizer ---
try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    print("Model and vectorizer loaded successfully.")
except FileNotFoundError:
    st.error(
        f"Model files not found. Please ensure '{MODEL_PATH}' and '{VECTORIZER_PATH}' exist. "
        "Run train.py first to generate them."
    )
    st.stop()

# --- Download NLTK stopwords (if not already present) ---
try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')

# --- Text Preprocessing Function ---
def clean_text(text):
    if not isinstance(text, str):
        text = str(text)
    # The 'count' parameter is deprecated and will be removed in a future version.
    # The re.sub function does not use a 'count' parameter in this way.
    # The flags re.I|re.A are also not standard for the 4th argument.
    # Correct usage is re.sub(pattern, repl, string, count=0, flags=0)
    text = re.sub(r'[^a-zA-Z\s]', '', text, flags=re.IGNORECASE)
    text = text.lower()
    text = text.strip()
    stop_words = set(stopwords.words('english'))
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# --- Streamlit Web App Interface ---
st.set_page_config(page_title="SQL Injection Detector", page_icon="🛡️")
st.title("🛡️ SQL Injection Detection using NLP")
st.write(
    "Enter a query or a piece of code below. The AI model will analyze it and predict "
    "if it's a potential SQL Injection attack or a benign statement."
)

user_input = st.text_area("Enter the text to analyze:", height=150, placeholder="e.g., SELECT * FROM users WHERE id = '1' OR '1'='1'")

if st.button("Analyze"):
    if user_input:
        cleaned_input = clean_text(user_input)
        vectorized_input = vectorizer.transform([cleaned_input])
        prediction = model.predict(vectorized_input)
        prediction_proba = model.predict_proba(vectorized_input)

        st.subheader("Analysis Result")
        
        if prediction[0] == 1:
            confidence = prediction_proba[0][1]
            st.error(f"Prediction: Malicious (SQL Injection)", icon="🚨")
            st.write(f"**Confidence:** {confidence:.2%}")
            st.warning(
                "**Reasoning:** The input text contains patterns commonly found in SQL injection attacks."
            )
        else:
            confidence = prediction_proba[0][0]
            st.success(f"Prediction: Benign (Safe)", icon="✅")
            st.write(f"**Confidence:** {confidence:.2%}")
            st.info(
                "**Reasoning:** The input text does not appear to contain common SQL injection syntax."
            )
    else:
        st.warning("Please enter some text to analyze.")

st.markdown("---")
st.write("Developed for CT201H - Computer Security Project.")
