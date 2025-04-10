from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import os
import pandas as pd

# Load individual datasets
nazario = pd.read_csv("data/Nazario.csv")
nigerian = pd.read_csv("data/Nigerian_Fraud.csv")
spamassassin = pd.read_csv("data/SpamAssasin.csv")

# Standardize column order just in case
common_cols = ['sender', 'receiver', 'date', 'subject', 'body', 'urls', 'label']
nazario = nazario[common_cols]
nigerian = nigerian[common_cols]
spamassassin = spamassassin[common_cols]

# Merge datasets
df = pd.concat([nazario, nigerian, spamassassin], ignore_index=True)

# Drop rows with missing senders or labels
df = df.dropna(subset=["sender", "label"])

# Only use sender email for classification
X = df["sender"]
y = df["label"]

# Convert sender email strings into numerical vectors
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# Split for safety (optional)
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and vectorizer
models_path = os.path.join(os.path.dirname(__file__), "../models")

with open(os.path.join(models_path, "sender_model.pkl"), "wb") as f:
    pickle.dump(model, f)

with open(os.path.join(models_path, "sender_vectorizer.pkl"), "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Sender model and vectorizer saved.")
