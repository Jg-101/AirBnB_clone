#!/usr/bin/env python3
""" Class Amenity in prog"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class Amenity that inherits BaseModel
        Public class attr
            name: (str) - amenity name in prog
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Init Amenity
            Args:
                *args: list of strs
                **kwargs: dict of strs
        """
        super().__init__(*args, **kwargs)
