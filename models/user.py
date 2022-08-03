#!/usr/bin/python3
"""
User class module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User which inherits from class BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
