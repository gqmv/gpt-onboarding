from langchain.agents.tools import tool
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

@tool
def set_categories_for_user(user_id: str, categories: list[Category]):
    """
    Set the categories for a user.
    
    Args:
        user_id (str): The user ID.
        categories (list[Category]): The categories to set.
    """
    
    print(f"!--- Pretend that the categories {categories} have been set for the user {user_id} ---!")

@tool
def set_frequency_for_user(user_id: str, frequency_days: int):
    """
    Set the frequency for which a user receives updates.
    
    Args:
        user_id (str): The user ID.
        frequency_days (int): The frequency in days.
    """
    
    print(f"!--- Pretend that the frequency {frequency_days} has been set for the user {user_id} ---!")
    
@tool
def set_prefered_time_for_user(user_id: str, time: int):
    """
    Set the time for which a user receives updates.
    
    Args:
        user_id (str): The user ID.
        time (int): The time in hours. (24-hour format)
    """
    
    print(f"!--- Pretend that the time {time} has been set for the user {user_id} ---!")
    
