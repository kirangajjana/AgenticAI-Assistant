# tools/base_tool.py
from abc import ABC, abstractmethod

class BaseTool(ABC):
    """Abstract Base Class for Tools"""

    @abstractmethod
    def execute(self, query: str):
        """Abstract method to execute the tool"""
        pass
