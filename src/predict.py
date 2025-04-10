import pickle
import joblib
import os

# Define path
base_path = os.path.dirname(__file__)

# === Load Email Content Classifier ===
with open(os.path.join(base_path, "../models/email_model.pkl"), "rb") as f:
    email_model = pickle.load(f)

with open(os.path.join(base_path, "../models/email_vectorizer.pkl"), "rb") as f:
    email_vectorizer = pickle.load(f)

# === Load URL Classifier ===
url_model = joblib.load(os.path.join(base_path, "../models/url_model.joblib"))

# === Load Sender Email ID Classifier ===
with open(os.path.join(base_path, "../models/sender_model.pkl"), "rb") as f:
    sender_model = pickle.load(f)

with open(os.path.join(base_path, "../models/sender_vectorizer.pkl"), "rb") as f:
    sender_vectorizer = pickle.load(f)

# === Prediction Functions ===
def predict_email(text):
    vectorized = email_vectorizer.transform([text])
    return "🚨 Phishing Email" if email_model.predict(vectorized)[0] == 1 else "✅ Safe Email"

def predict_url(url):
    return "🚨 Phishing URL" if url_model.predict([url])[0] == 1 else "✅ Safe URL"

def predict_sender(email):
    vect = sender_vectorizer.transform([email])
    return "🚨 Fraudulent Email ID" if sender_model.predict(vect)[0] == 1 else "✅ Safe Email ID"
