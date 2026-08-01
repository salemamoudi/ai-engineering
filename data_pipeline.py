from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np

print("=" * 50)
print("Building a Data Pipeline")
print("=" * 50)

# Load data
data = {
    "text": [
        "This movie was absolutely amazing! The acting was superb.",
        "Terrible film, complete waste of time. I walked out early.",
        "Great acting and an incredible story. Highly recommend!",
        "I hated every minute of it. Boring and predictable.",
        "Pretty good, I recommend it to anyone who likes this genre.",
        "Not my cup of tea, but well made and acted.",
        "Couldn't stop watching! Brilliant from start to finish.",
        "Underwhelming. Expected much more from the director.",
        "A masterpiece of modern cinema. Must watch!",
        "Too long and slow paced. Could have been shorter."
    ],
    "label": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

print(f"\n📊 Dataset size: {len(df)}")
print(f"   Positive reviews: {sum(df['label'])}")
print(f"   Negative reviews: {len(df) - sum(df['label'])}")

# Step 1: Split data
X = df['text']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\n📊 Split:")
print(f"   Training set: {len(X_train)} samples")
print(f"   Test set: {len(X_test)} samples")

# Step 2: Feature extraction (word counts)
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

print(f"\n📊 Feature extraction:")
print(f"   Vocabulary size: {len(vectorizer.get_feature_names_out())}")
print(f"   Training matrix shape: {X_train_vec.shape}")

# Step 3: Show sample features
print(f"\n📊 Sample features:")
features = vectorizer.get_feature_names_out()[:10]
print(f"   First 10 features: {features.tolist()}")

print("\n✅ Data pipeline complete!")
