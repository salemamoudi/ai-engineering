#!/usr/bin/env python
"""
Test API Connections
Verifies that all API keys are working
"""

import sys
import config

def test_openai():
    """Test OpenAI API connection"""
    print("Testing OpenAI API...")
    if not config.Config.has_key('OPENAI_API_KEY'):
        print("  ❌ OpenAI key not set")
        return False
    
    try:
        from openai import OpenAI
        client = OpenAI(api_key=config.Config.OPENAI_API_KEY)
        
        # Test with a simple completion
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'Hello AI Engineering!'"}],
            max_tokens=20
        )
        print(f"  ✅ OpenAI working: {response.choices[0].message.content}")
        return True
    except Exception as e:
        print(f"  ❌ OpenAI error: {e}")
        return False

def test_anthropic():
    """Test Anthropic API connection"""
    print("Testing Anthropic API...")
    if not config.Config.has_key('ANTHROPIC_API_KEY'):
        print("  ❌ Anthropic key not set")
        return False
    
    try:
        from anthropic import Anthropic
        client = Anthropic(api_key=config.Config.ANTHROPIC_API_KEY)
        
        # Test with a simple completion
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=20,
            messages=[{"role": "user", "content": "Say 'Hello AI Engineering!'"}]
        )
        print(f"  ✅ Anthropic working: {response.content[0].text}")
        return True
    except Exception as e:
        print(f"  ❌ Anthropic error: {e}")
        return False

def test_huggingface():
    """Test Hugging Face API connection"""
    print("Testing Hugging Face API...")
    if not config.Config.has_key('HUGGINGFACE_API_KEY'):
        print("  ❌ Hugging Face key not set")
        return False
    
    try:
        from huggingface_hub import HfApi
        api = HfApi(token=config.Config.HUGGINGFACE_API_KEY)
        user = api.whoami()
        print(f"  ✅ Hugging Face working: {user.get('name', 'Unknown')}")
        return True
    except Exception as e:
        print(f"  ❌ Hugging Face error: {e}")
        return False

def main():
    print("=" * 60)
    print("API Connection Test")
    print("=" * 60)
    print()
    
    # Show key status
    config.Config.print_status()
    print()
    
    # Test each API
    results = {
        "OpenAI": test_openai(),
        "Anthropic": test_anthropic(),
        "Hugging Face": test_huggingface()
    }
    
    print()
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    
    total = len(results)
    passed = sum(1 for v in results.values() if v)
    
    print(f"✅ Passed: {passed}/{total}")
    print()
    
    # Show details
    for service, status in results.items():
        status_icon = "✅" if status else "❌"
        print(f"{status_icon} {service}: {'Working' if status else 'Failed'}")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
