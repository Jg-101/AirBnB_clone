#!/usr/bin/env python3
""" class City in prog """
from models.base_model import BaseModel


class City(BaseModel):
    """ Class City that inherits BaseModel
        Pub class attr
            state_id: (str) - State.id
            name: (str) - City name
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Init City
            Args:
                *args: list of strs
                **kwargs: dict of strs"""
        super().__init__(*args, **kwargs)
