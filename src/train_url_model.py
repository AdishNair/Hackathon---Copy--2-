import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
df = pd.read_csv("data/urls.csv", encoding="utf-8")

# Make sure 'url' and 'type' columns exist
df = df[['url', 'type']]

# Drop rows with NaN in 'type' or 'url'
df = df.dropna(subset=['url', 'type'])

# Encode 'type' column: phishing = 1, legitimate = 0
df['label'] = df['type'].apply(lambda x: 1 if x.lower() == 'phishing' else 0)

# Features and target
X = df['url']
y = df['label']

# Just to be safe, drop any remaining NaNs
X = X.fillna("")
y = y.fillna(0)

# Create model pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

# Train the model
model.fit(X, y)

# Save the trained model
joblib.dump(model, "models/url_model.joblib")
