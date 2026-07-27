"""Unified AI Client for multiple APIs"""

import config

class AIClient:
    """Unified client for various AI APIs"""
    
    def __init__(self):
        self.openai_client = None
        self.anthropic_client = None
        self._init_clients()
    
    def _init_clients(self):
        """Initialize available API clients"""
        try:
            if config.Config.has_key('OPENAI_API_KEY'):
                from openai import OpenAI
                self.openai_client = OpenAI(api_key=config.Config.OPENAI_API_KEY)
        except:
            pass
        
        try:
            if config.Config.has_key('ANTHROPIC_API_KEY'):
                from anthropic import Anthropic
                self.anthropic_client = Anthropic(api_key=config.Config.ANTHROPIC_API_KEY)
        except:
            pass
    
    def query_openai(self, prompt: str) -> str:
        """Query OpenAI"""
        if not self.openai_client:
            return "❌ OpenAI client not initialized"
        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"❌ OpenAI error: {e}"
    
    def query_anthropic(self, prompt: str) -> str:
        """Query Anthropic"""
        if not self.anthropic_client:
            return "❌ Anthropic client not initialized"
        try:
            response = self.anthropic_client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=1000,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            return f"❌ Anthropic error: {e}"

if __name__ == "__main__":
    client = AIClient()
    print("Testing OpenAI:", client.query_openai("What is AI Engineering?"))
    print("Testing Anthropic:", client.query_anthropic("What is AI Engineering?"))
