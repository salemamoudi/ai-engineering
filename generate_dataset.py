import requests
import pandas as pd
from datasets import Dataset
import time

def ask_ollama(prompt, model="tinyllama"):
    """Send prompt to Ollama"""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=120
        )
        return response.json().get('response', '')
    except Exception as e:
        return f"Error: {e}"

print("=" * 50)
print("Generating Dataset with Ollama")
print("=" * 50)

# Prompts for generating reviews
prompts = [
    "Write a positive movie review:",
    "Write a negative movie review:",
    "Write a positive TV show review:",
    "Write a negative TV show review:",
]

reviews = []
labels = []

for prompt in prompts:
    print(f"\n📝 Generating: {prompt}")
    response = ask_ollama(prompt)
    reviews.append(response)
    labels.append(1 if "positive" in prompt else 0)
    print(f"   ✅ Generated: {response[:100]}...")
    time.sleep(1)  # Be nice to Ollama

# Create dataset
df = pd.DataFrame({"text": reviews, "label": labels})
dataset = Dataset.from_pandas(df)

print(f"\n📊 Generated dataset:")
print(f"   Size: {len(dataset)}")
print(f"   Positive: {sum(dataset['label'])}")
print(f"   Negative: {len(dataset) - sum(dataset['label'])}")

print("\n📝 Sample:")
for i in range(min(2, len(dataset))):
    print(f"   {i+1}. {dataset['text'][i][:100]}... (Label: {dataset['label'][i]})")

print("\n✅ Dataset generation complete!")
