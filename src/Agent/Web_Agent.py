# src/Agent/Web_Agent.py
from src.Agent.Base_Agent import BaseAgent  # ✅ Match exact folder name


class WebAgent(BaseAgent):
    """Concrete Web Agent Implementation"""

    
    def respond(self, query: str, stream=False):
            """AI Agent first searches for external sources before responding."""

            # Step 1: Use the Search Tool First
            if self.tools:
                search_results = self.tools[0].execute(query)  # Uses DuckDuckGo/Google Search
                if search_results and isinstance(search_results, list):  
                    sources = "\n".join([f"- [{r['title']}]({r['link']})" for r in search_results])
                    knowledge_base = f"Here are the top sources I found:\n{sources}\n\n"
                else:
                    knowledge_base = "I couldn't find any relevant sources. Let me try answering from my knowledge.\n\n"
            else:
                knowledge_base = "No search tool is available. Answering from my internal knowledge.\n\n"

            # Step 2: Combine Search Results with AI Response
            full_query = f"{knowledge_base}User Query: {query}"
            response = self.model.generate_response(full_query)

            return response
