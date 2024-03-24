#!/usr/bin/python3
"""Module is made up of the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents the Review model"""
    place_id = ""
    user_id = ""
    text = ""
