from src.Tools.Base_Tool import BaseTool
from duckduckgo_search import DDGS

class DuckDuckGoTool(BaseTool):
    """Concrete Implementation of DuckDuckGo Search Tool for Agentic AI Articles"""

    def __init__(self):
        """Initialize DuckDuckGo search tool"""
        self.tool = DDGS()

    def execute(self, query: str):
        """
        Perform a DuckDuckGo search and **ensure results are real**.

        Args:
            query (str): The search query.

        Returns:
            list: Top 5 search results with title and URL.
        """
        try:
            modified_query = f"{query} Agentic AI artificial intelligence"

            # Fetch real data
            results = self.tool.text(modified_query, max_results=5)

            if not results:
                return [{"title": "No real articles found", "link": "#"}]

            return [{"title": r["title"], "link": r["href"]} for r in results]

        except Exception as e:
            return [{"title": "Search Error", "link": "#", "error": str(e)}]
