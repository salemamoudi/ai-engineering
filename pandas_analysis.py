import pandas as pd
import numpy as np

print("=" * 50)
print("Pandas Data Analysis")
print("=" * 50)

# Create sample data
data = {
    "text": [
        "This movie was absolutely amazing! The acting was superb.",
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

print(f"\n📊 DataFrame shape: {df.shape}")
print(f"\nFirst 5 rows:")
print(df.head())

# Analyze text length
df['text_length'] = df['text'].str.len()
print(f"\n📊 Text length statistics:")
print(df['text_length'].describe())

# Label distribution
print(f"\n📊 Label distribution:")
print(df['label'].value_counts())

# Group by label
print(f"\n📊 Average text length by label:")
print(df.groupby('label')['text_length'].mean())

# Find longest and shortest reviews
longest_idx = df['text_length'].idxmax()
shortest_idx = df['text_length'].idxmin()
print(f"\n📊 Longest review ({df.loc[longest_idx, 'text_length']} chars):")
print(f"  {df.loc[longest_idx, 'text'][:100]}...")
print(f"\n📊 Shortest review ({df.loc[shortest_idx, 'text_length']} chars):")
print(f"  {df.loc[shortest_idx, 'text']}")

print("\n✅ Analysis complete!")
