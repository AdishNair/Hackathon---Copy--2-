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

# Display class distribution (optional)
print(df["label"].value_counts())
