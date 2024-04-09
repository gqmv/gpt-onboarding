from openai import OpenAI
from langchain.agents.openai_assistant import OpenAIAssistantRunnable
from langchain.agents import AgentExecutor
from langchain.tools import BaseTool
from services.OpenAIFunctions import set_categories_for_user, set_frequency_for_user, set_prefered_time_for_user

MODEL = "gpt-4-turbo-preview"
NAME = "Everything Newsletter"
INSTRUCTIONS = """You are a Everything Newsletter, a helpful newsletter that sends personalized updates.
You are a telegram bot. Make your answers short and to the point.
Your objective is to collect information about the following:
What are the user's interests? (Ask for 3 categories of interest at first, but allow the user to add more)
What is the user's preferred frequency for receiving updates? (Ask for a number of days)
What is the user's preferred time for receiving updates? (Ask for a time in hours, 24-hour format)
When you have collected this information, you can let the user know that you will start sending them updates based on their preferences.
"""
TOOLS = [set_categories_for_user, set_frequency_for_user, set_prefered_time_for_user]

threads = {}

class OpenAIService:
    def __init__(self, api_key: str):
        self._api_key = api_key
        self._agent: AgentExecutor | None = None
    
    def get_agent(self) -> AgentExecutor:
        """Gets an OpenAI assistant instance."""
        if not self._agent:
            client = OpenAI(api_key=self._api_key)
            assistant = OpenAIAssistantRunnable.create_assistant(
                name=NAME,
                instructions=INSTRUCTIONS,
                tools=TOOLS,
                model=MODEL,
                as_agent=True,
                client=client,
            )
            
            self._agent = AgentExecutor(
                agent=assistant,
                tools=TOOLS,
            )
        return self._agent
        
    def get_thread_id(self, user_id: str):
        """Get a thread for a user."""
        if user_id not in threads:
            return None
        return threads[user_id]
    
    
    def get_response(self, user_id: str, message: str) -> str:
        """Get a response from the OpenAI assistant."""
        content = {"content": message}
        
        thread_id = self.get_thread_id(user_id)
        
        if thread_id:
            content["thread_id"] = thread_id
        
        response = self.get_agent().invoke(content, user_id=user_id)
        new_thread_id = response["thread_id"]
        
        threads[user_id] = new_thread_id
        
        output = response["output"]
        return output
        
    

            
            
        