#!/usr/bin/env python3
""" Class place in prog"""
from models.base_model import BaseModel


class State(BaseModel):
    """ Class place that inherits from BaseModel
        Public class attrs:
            name: (str) - Name of the state
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Init class attrs
            Args:
                *args: list of strs
                **kwargs: dict of strs
        """
        super().__init__(*args, **kwargs)
