# models/base_model.py
from abc import ABC, abstractmethod

class BaseModel(ABC):
    """Abstract Base Class for AI Models"""

    @abstractmethod
    def generate_response(self, query: str, tools=None):
        """Abstract method for generating AI responses"""
        pass
