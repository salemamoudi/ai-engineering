"""Test API Connections"""

import config

def test_openai():
    """Test OpenAI API"""
    print("Testing OpenAI API...")
    if not config.Config.has_key('OPENAI_API_KEY'):
        print("  ❌ OpenAI key not set")
        return False
    
    try:
        from openai import OpenAI
        client = OpenAI(api_key=config.Config.OPENAI_API_KEY)
        
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
    """Test Anthropic API"""
    print("Testing Anthropic API...")
    if not config.Config.has_key('ANTHROPIC_API_KEY'):
        print("  ❌ Anthropic key not set")
        return False
    
    try:
        from anthropic import Anthropic
        client = Anthropic(api_key=config.Config.ANTHROPIC_API_KEY)
        
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
    """Test Hugging Face API"""
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
    
    config.Config.print_status()
    print()
    
    results = {
        "OpenAI": test_openai(),
        "Anthropic": test_anthropic(),
        "Hugging Face": test_huggingface()
    }
    
    print()
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    print(f"✅ Passed: {passed}/{total}")
    
    for service, status in results.items():
        icon = "✅" if status else "❌"
        print(f"{icon} {service}: {'Working' if status else 'Failed'}")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
