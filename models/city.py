from models.base_model import BaseModel
"""
base city.py
Created by Rewan Abdulkariem @11/4/2024
"""
class City(BaseModel):
    """
    Represents a city.

    Attributes:
        state_id (str): The id of the state to which the city belongs.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
