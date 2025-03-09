# src/Agent/Web_Agent.py
from src.Agent.Base_Agent import BaseAgent  # ✅ Match exact folder name


class WebAgent(BaseAgent):
    """Concrete Web Agent Implementation"""

    
    def respond(self, query: str, stream=False):
        """AI Agent only answers queries related to Agentic AI. Otherwise, it responds with a default message."""

        # Define allowed topics
        allowed_keywords = ["Agentic AI", "AI Agents", "Multi-Agent Systems", "Autonomous Agents", "AI-powered research"]

        # Step 1: Check if the Query is Relevant
        if not any(keyword.lower() in query.lower() for keyword in allowed_keywords):
            return "⚠️ I specialize in Agentic AI research. I don't have information on this topic."

        # Step 2: Use Search Tool First (if available)
        knowledge_base = ""
        if self.tools:
            search_results = self.tools[0].execute(query)
            if search_results and isinstance(search_results, list):  
                sources = "\n".join([f"- [{r['title']}]({r['link']})" for r in search_results])
                knowledge_base = f"Here are the top sources I found:\n{sources}\n\n"
            else:
                knowledge_base = "I could not find relevant sources. Let me generate an answer based on my knowledge.\n\n"

        # Step 3: Combine Search Results with AI Response
        full_query = f"{knowledge_base}User Query: {query}"
        response = self.model.generate_response(full_query)

        return response

        