# agents/base_agent.py
from abc import ABC, abstractmethod
from typing import List, Any, Optional

class BaseAgent(ABC):
    """Abstract Base Class for AI Agents"""

    def __init__(
        self, 
        name: str, 
        model: Any, 
        tools: Optional[List[Any]] = None, 
        instructions: Optional[List[str]] = None, 
        description: Optional[str] = None, 
        knowledge: Optional[List[str]] = None, 
        memory: Optional[List[str]] = None
    ):
        """
        Initialize the base agent.

        Args:
            name (str): Name of the agent.
            model (Any): AI model associated with the agent.
            tools (Optional[List[Any]]): List of tools the agent can use.
            instructions (Optional[List[str]]): Set of instructions for the agent.
            description (Optional[str]): Description of the agent's purpose.
            knowledge (Optional[List[str]]): Stored knowledge of the agent.
            memory (Optional[List[str]]): Persistent memory of past interactions.
        """
        self.name = name
        self.model = model
        self.tools = tools or []
        self.instructions = instructions or []
        self.description = description or ""
        self.knowledge = knowledge or []
        self.memory = memory or []

    @abstractmethod
    def respond(self, query: str) -> str:
        """Abstract method for generating responses"""
        pass
