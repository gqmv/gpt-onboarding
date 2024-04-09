from openai import OpenAI
from langchain.agents.openai_assistant import OpenAIAssistantRunnable
from langchain.agents import AgentExecutor
from langchain.tools import BaseTool
from functools import partial
import copy
from services.OpenAIFunctions import set_days_for_user, set_categories_for_user, set_prefered_time_for_user

MODEL = "gpt-4-turbo-preview"
NAME = "Everything Newsletter"
INSTRUCTIONS = """You are a Everything Newsletter, a helpful newsletter that sends personalized updates.
You are a telegram bot. Make your answers short and to the point.
Your objective is to collect information about the following and set the values using the tools provided:
What are the user's interests? (Ask for 3 categories of interest at first, but allow the user to add more or less.)
What is the user's preferred days for receiving updates? (The user may select multiple days of the week. This defaults to every day, but the user can change it.)
What is the user's preferred time for receiving updates? (Ask for a time in hours, 24-hour format)

When you have collected this information, you can let the user know that you will start sending them updates based on their preferences.
"""
TOOLS = [set_categories_for_user, set_days_for_user, set_prefered_time_for_user]

threads = {}

class OpenAIService:
    def __init__(self, api_key: str):
        self._api_key = api_key
        self._openai_agent = None
        
    def _get_openai_agent(self) -> OpenAIAssistantRunnable:
        """Gets an OpenAI assistant instance."""
        if not self._openai_agent:
            client = OpenAI(api_key=self._api_key)
            self._openai_agent = OpenAIAssistantRunnable.create_assistant(
                name=NAME,
                instructions=INSTRUCTIONS,
                tools=TOOLS,
                model=MODEL,
                as_agent=True,
                client=client,
            )
        return self._openai_agent
        
    
    def get_agent(self, user_id: str) -> AgentExecutor:
        """Gets an agent executor instance, bound to a specific user."""
        openai_agent = self._get_openai_agent()
        
        # The following is a workaround to pass the user_id to the tools.
        # A copy of the tools is created and the user_id is passed to each tool as a partial function call.
        # If in doubt (probably never learned haskell heh?) contact @gqmv.
        tools = copy.deepcopy(TOOLS)
        for tool in tools:
            tool.func = partial(tool.func, user_id=user_id)
        
        agent = AgentExecutor(
            agent=openai_agent,
            tools=tools,
        )
        return agent
        
        
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
        
        response = self.get_agent(user_id=user_id).invoke(content)
        new_thread_id = response["thread_id"]
        
        threads[user_id] = new_thread_id
        
        output = response["output"]
        return output
        
    

            
            
        