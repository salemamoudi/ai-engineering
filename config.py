
"""
Configuration Module
Loads environment variables from .env file
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

class Config:
    """Configuration class for API keys and settings"""
    
    # OpenAI
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_ORGANIZATION = os.getenv('OPENAI_ORGANIZATION')
    
    # Anthropic
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
    
    # Hugging Face
    HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
    
    # Debug mode
    DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    @classmethod
    def get_key(cls, key_name: str) -> str:
        """Get an API key by name, raise error if missing"""
        value = getattr(cls, key_name, None)
        if not value:
            raise ValueError(f"API key '{key_name}' not found. Please set it in .env file")
        return value
    
    @classmethod
    def has_key(cls, key_name: str) -> bool:
        """Check if an API key exists"""
        return bool(getattr(cls, key_name, None))
    
    @classmethod
    def print_status(cls):
        """Print the status of all API keys"""
        print("=" * 50)
        print("API Key Status")
        print("=" * 50)
        
        keys = [
            'OPENAI_API_KEY',
            'ANTHROPIC_API_KEY', 
            'HUGGINGFACE_API_KEY'
        ]
        
        for key in keys:
            status = "✅" if cls.has_key(key) else "❌"
            print(f"{status} {key}: {'✓ Set' if cls.has_key(key) else 'Not set'}")
        
        print("=" * 50)

if __name__ == "__main__":
    Config.print_status()
