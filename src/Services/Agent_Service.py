from src.Agent.Web_Agent import WebAgent
from src.Models.OpenAI_Model import OpenAIModel
from src.Tools.Google_Search_Tool import DuckDuckGoTool

class AgentService:
    """Service Layer to Handle Agent Interactions"""

    def __init__(self):
        self.model = OpenAIModel()

        # ✅ Use the updated DuckDuckGo search tool
        self.tool = DuckDuckGoTool()

        self.agent = WebAgent(
            name="Web Agent",
            model=self.model,
            tools=[self.tool],
            description="AI Agent specialized in finding top articles on Agentic AI.",
            instructions=[
                "Always provide articles and research materials related to AI agents.",
                "Prioritize results that discuss Agentic AI.",
                "Ensure the sources are relevant and high-quality."
            ],
            knowledge=["Specialized in AI Agents and Agentic AI research."],
            memory=[]
        )

    def handle_query(self, query):
        """Handles agent query and ensures it retrieves relevant AI Agent articles"""
        return self.agent.respond(query, stream=True)



