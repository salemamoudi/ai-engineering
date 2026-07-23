import pandas as pd
from datasets import Dataset

print("=" * 50)
print("Lesson 09: Data Management - Local Dataset")
print("=" * 50)

# Create a larger, more realistic dataset
data = {
    "text": [
        "This movie was absolutely amazing! The acting was superb, and the story kept me hooked.",
        "Terrible film, complete waste of time. I walked out early and demanded a refund.",
        "Great acting and an incredible story. Highly recommend to everyone!",
        "I hated every minute of it. Boring, predictable, and poorly acted.",
        "Pretty good, I recommend it to anyone who likes this genre.",
        "Not my cup of tea, but I can see why others might enjoy it.",
        "Couldn't stop watching! Brilliant from start to finish.",
        "Underwhelming. Expected much more from such a famous director.",
        "A masterpiece of modern cinema. Absolutely must watch!",
        "Too long and slow paced. Could have been edited down significantly.",
        "Excellent performances and beautiful cinematography.",
        "Disappointing sequel. The original was much better.",
        "Heartwarming story with great characters. Loved every moment.",
        "Predictable plot with cliché dialogue. Disappointing.",
        "Visually stunning and thought-provoking. A great experience."
    ],
    "label": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)
dataset = Dataset.from_pandas(df)

print(f"\n✅ Dataset created successfully!")
print(f"Total samples: {len(dataset)}")
print(f"Features: {dataset.features}")
print(f"Label distribution:")
print(f"  Positive: {sum(dataset['label'])}")
print(f"  Negative: {len(dataset) - sum(dataset['label'])}")

print("\n📊 Sample data:")
for i in range(3):
    print(f"  {i+1}. {dataset['text'][i][:60]}... (Label: {dataset['label'][i]})")

print("\n✅ Dataset ready for analysis!")
