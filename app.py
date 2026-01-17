%%writefile app.py
import streamlit as st
import re
import pickle

# Load saved objects
model = pickle.load(open("model.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

st.title("AI Content Moderation System")

user_input = st.text_area("Enter a comment to check toxicity:")

if st.button("Check Toxicity"):
    clean = clean_text(user_input)
    vector = tfidf.transform([clean])
    prediction = model.predict(vector)[0]
    probability = model.predict_proba(vector)[0][1]

    if prediction == 1:
        st.error(f"Toxic Content Detected 🚨 (Confidence: {probability:.2f})")
    else:
        st.success(f"Non-Toxic Content ✅ (Confidence: {1 - probability:.2f})")
