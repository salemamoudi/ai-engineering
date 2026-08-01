import pandas as pd
import numpy as np

print("=" * 50)
print("Pandas Data Analysis")
print("=" * 50)

# Create sample data
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

print(f"\n📊 DataFrame Info:")
print(f"   Shape: {df.shape}")
print(f"   Columns: {df.columns.tolist()}")

print(f"\n📊 First 3 rows:")
print(df.head(3))

# Analyze text lengths
df['text_length'] = df['text'].str.len()
df['word_count'] = df['text'].str.split().str.len()

print(f"\n📊 Text Statistics:")
print(df[['text_length', 'word_count']].describe())

# Label distribution
print(f"\n📊 Label Distribution:")
print(df['label'].value_counts())

# Average text length by label
print(f"\n📊 Average Text Length by Label:")
print(df.groupby('label')['text_length'].mean())

print("\n✅ Analysis complete!")
