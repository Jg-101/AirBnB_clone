#!/usr/bin/env python3
""" Class User in prog"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Class user that inherits from BaseModel
        Pub class attrs:
            email: (str) - user's email
            password: (str) - user's password
            first_name: (str) - user's first name
            last_name: (str) - user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Init class User
            Args:
                *args: list of strs
                **kwargs: dict of strs
                """
        super().__init__(*args, **kwargs)
