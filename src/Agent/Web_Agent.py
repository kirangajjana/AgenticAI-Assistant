# src/Agent/Web_Agent.py
from src.Agent.Base_Agent import BaseAgent  # ✅ Match exact folder name


class WebAgent(BaseAgent):
    """Concrete Web Agent Implementation"""

    def respond(self, query: str, stream=False):
        """Generate a response using the model and tools"""
        response = self.model.generate_response(query, self.tools)
        if stream:
            print(f"[{self.name}] Streaming Response: {response}")
        else:
            print(f"[{self.name}] Response: {response}")
        return response
