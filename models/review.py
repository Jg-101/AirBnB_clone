#!/usr/bin/env python3
""" Class Review in prog"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Pub class attrs:

    place_id: str - (str): Place.id
    user_id: str - (str): User.id
    txt: str - (str): text of the review
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Init a Review instance
            Args:
                *args: list of strs
                **kwargs: dict of strs
        """
        super().__init__(*args, **kwargs)
