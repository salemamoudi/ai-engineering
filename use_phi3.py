#!/usr/bin/env python
"""
Use Phi-3 model via Ollama - Free and Local!
"""

import requests
import json

def ask_phi3(prompt):
    """Send a prompt to Phi-3 model"""
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "phi3",
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json().get('response', '')
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {e}"

# Test the model
print("=" * 50)
print("Phi-3 Test (Local AI - Free!)")
print("=" * 50)

questions = [
    "What is AI Engineering in one sentence?",
    "What are the main topics in AI Engineering?",
    "Why is it important to learn AI from scratch?"
]

for q in questions:
    print(f"\nQ: {q}")
    response = ask_phi3(q)
    print(f"A: {response}")
    print("-" * 40)
