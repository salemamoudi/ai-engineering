from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

print("=" * 50)
print("Data Pipeline")
print("=" * 50)

# Create dataset
data = {
    "text": [
        "This movie was absolutely amazing!",
        "Terrible film, complete waste of time.",
        "Great acting and an incredible story.",
        "I hated every minute of it.",
        "Pretty good, I recommend it.",
        "Not my cup of tea, but well made.",
        "Couldn't stop watching! Brilliant!",
        "Underwhelming. Expected much more.",
        "A masterpiece of modern cinema.",
        "Too long and slow paced."
    ],
    "label": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

print(f"\n📊 Dataset size: {len(df)}")

# Step 1: Split data
X = df['text']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\n📊 Split:")
print(f"  Training set: {len(X_train)} samples")
print(f"  Test set: {len(X_test)} samples")

# Step 2: Feature extraction (simple word count)
def word_count(text):
    return len(text.split())

X_train_wc = X_train.apply(word_count)
X_test_wc = X_test.apply(word_count)

print(f"\n📊 Training set word count statistics:")
print(f"  Min: {X_train_wc.min()}")
print(f"  Max: {X_train_wc.max()}")
print(f"  Mean: {X_train_wc.mean():.2f}")

print(f"\n📊 Test set word count statistics:")
print(f"  Min: {X_test_wc.min()}")
print(f"  Max: {X_test_wc.max()}")
print(f"  Mean: {X_test_wc.mean():.2f}")

# Step 3: Display sample
print(f"\n📊 Training sample:")
for i in range(min(3, len(X_train))):
    print(f"  Text: {X_train.iloc[i]}")
    print(f"  Label: {y_train.iloc[i]}")
    print(f"  Word count: {X_train_wc.iloc[i]}")
    print("---")

print("\n✅ Data pipeline complete!")
