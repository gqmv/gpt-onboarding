from langchain.agents.tools import tool
from langchain.pydantic_v1 import BaseModel, Field
from datetime import time
from enum import Enum

class Category(Enum):
    web3 = "web3"
    defi = "defi"
    artificial_intelligence = "artificial_intelligence"
    machine_learning = "machine_learning"
    data_science = "data_science"
    blockchain = "blockchain"
    business = "business"
    finance = "finance"
    technology = "technology"
    memes = "memes"
    urbanism = "urbanism"
    cocktails = "cocktails"
    martial_arts = "martial_arts"

class SetCategoriesInput(BaseModel):
    categories: list[Category] = Field(title="The categories to set for the user.")

@tool("set_categories_for_user", args_schema=SetCategoriesInput)
def set_categories_for_user(user_id: str, categories: list[Category]):
    """
    Set the categories that a user is interested in.
    """
    
    print(f"!--- Pretend that the categories {categories} have been set for the user {user_id} ---!")

class Weekday(Enum):
    monday = "monday"
    tuesday = "tuesday"
    wednesday = "wednesday"
    thursday = "thursday"
    friday = "friday"
    saturday = "saturday"
    sunday = "sunday"
    
class SetDaysInput(BaseModel):
    days: list[Weekday] = Field(title="The days at which the user receives updates.")


@tool(
    "set_days_for_user",
    args_schema=SetDaysInput
)
def set_days_for_user(user_id: str, days: list[Weekday]):
    """
    Set the frequency for which a user receives updates.
    """
    
    print(f"!--- Pretend that the days {days} have been set for the user {user_id} ---!")
    
class SetTimeInput(BaseModel):
    update_time: time = Field(title="The time at which the user receives updates.")

    
@tool(
    "set_prefered_time_for_user",
    args_schema=SetTimeInput
)
def set_prefered_time_for_user(user_id: str, update_time: time):
    """
    Set the time at which the user receives updates.
    """
    
    print(f"!--- Pretend that the time {update_time} has been set for the user {user_id} ---!")
    
