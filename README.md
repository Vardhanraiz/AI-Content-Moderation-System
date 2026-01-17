# AI Content Moderation System

An AI-based content moderation system that detects toxic or abusive text using Natural Language Processing (NLP) and Machine Learning.  
This project demonstrates an end-to-end ML pipeline from data preprocessing to deployment.

---

## 🔍 Problem Statement
Online platforms receive a large volume of user-generated content. Manual moderation is slow and inconsistent.  
This project aims to automatically identify toxic comments to assist content moderation systems.

---

## 🧠 Solution Overview
The system processes raw text input, converts it into numerical features using TF-IDF, and classifies it using a Logistic Regression model.  
A threshold-based decision mechanism allows control over moderation strictness.

---

## ⚙️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- TF-IDF Vectorizer
- Streamlit

---

## 📂 Project Workflow
1. Data loading and exploration  
2. Text preprocessing (lowercasing, punctuation removal)  
3. Feature extraction using TF-IDF  
4. Model training with Logistic Regression  
5. Model evaluation using precision, recall, F1-score  
6. Threshold tuning for moderation control  
7. Deployment using Streamlit  

---

## 📊 Model Evaluation
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

Recall is prioritized to reduce missed toxic content.

---

## 🧪 Example Prediction
Input: You are a stupid idiot

Output:
Toxic Content Detected
Confidence: 0.89

---

## 🖥️ Web Application
The trained model is deployed using Streamlit, allowing users to:
- Enter custom text
- Adjust moderation strictness using a threshold slider
- View toxicity prediction and confidence score

---

## ⚠️ Limitations
- Struggles with sarcasm and contextual meaning
- Supports English text only
- Performance depends on training data quality

---

## 🚀 Future Improvements
- Multi-label toxicity classification
- Advanced NLP models (LSTM/BERT)
- Support for multiple languages

---

## 👤 Author
Final-year B.Tech CSE student  
This project is built for learning and academic demonstration purposes.


