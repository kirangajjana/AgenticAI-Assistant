import os
from src.Models.Base_Model import BaseModel
from phi.model.openai import OpenAIChat # ✅ Correct for phidata package
from dotenv import load_dotenv
from phi.model.openai.chat import Message
load_dotenv()


class OpenAIModel(BaseModel):
    """Concrete Implementation of OpenAI Model"""

    def __init__(self, model_id="gpt-4o"):
        self.api_key = os.getenv("OPENAI_API_KEY")  # Fetch API key from environment
        if not self.api_key:
            raise ValueError("OpenAI API key not found. Set OPENAI_API_KEY as an environment variable.")

        self.model = OpenAIChat(id=model_id, api_key=self.api_key,temperature=0)

    def generate_response(self, query: str, tools=None):
        """Corrected method call to OpenAI API"""
        messages = [Message(role="user", content=query)]  # ✅ Convert dict to Message object

        response = self.model.invoke(messages=messages)  # ✅ Use correct format

        return response.choices[0].message.content  # ✅ Extract text response# Extract text response



