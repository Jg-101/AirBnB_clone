#!/usr/bin/env python3
"""" Class place in prog"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Class place inherits from BaseModel
    Pub class attrs:
        city_id: str - (str): City.id
        user_id: str - (str): User.id
        name: (str) - Name of the place
        description: (str) - Desc of the place
        number_rooms: (int) - Num of rooms of the place
        number_bathrooms: (int) - Num of bathrooms of the place
        max_guest: (int) - Max num of guests that can be accommodated
        price_by_night: (int) - Price per night
        latitude: (float) - Latitude of the place
        longitude: (float) - Longitude of the place
        amenity_ids: (list) - List of Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ Init class Place
            Args:
                *args: list of strs
                **kwargs: dict of strs
                """
        super().__init__(*args, **kwargs)
