from datasets import load_dataset

print("=" * 50)
print("Exploring Hugging Face Datasets")
print("=" * 50)

# Try to load the IMDB dataset
print("\nLoading IMDB dataset...")
try:
    imdb = load_dataset("imdb")
    print(f"✅ IMDB dataset loaded successfully!")
    print(f"   Features: {imdb['train'].features}")
    print(f"   Training set: {len(imdb['train'])} samples")
    print(f"   Test set: {len(imdb['test'])} samples")
    
    # Look at a sample
    print(f"\n📝 Sample review:")
    sample = imdb['train'][0]
    print(f"   Text: {sample['text'][:200]}...")
    print(f"   Label: {sample['label']} (0=negative, 1=positive)")
except Exception as e:
    print(f"❌ Could not load IMDB dataset: {e}")
    print("   Using local dataset instead...")
    
    # Option B: Local dataset (fallback)
    import pandas as pd
    from datasets import Dataset
    
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
    dataset = Dataset.from_pandas(df)
    print("✅ Local dataset created with 10 samples!")
    print(f"   Features: {dataset.features}")
    print(f"   Size: {len(dataset)}")
