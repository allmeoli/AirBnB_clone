#!/usr/bin/python3
import copy
import uuid
from datetime import datetime


class BaseModel:
    """ Base model """

    def __init__(self, **kwargs):
        """public instance"""
        if kwargs != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return str representations"""
        return "[{}] ({}) {}".format (self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Edit the updated time """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of the instance"""
        dic = copy.deepcopy(self.__dict__)
        dic['id'] = str(dic['id'])
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = dic['created_at'].isoformat()
        dic['updated_at'] = dic['updated_at'].isoformat()
        return dic