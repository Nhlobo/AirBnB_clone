#!/usr/bin/python3
"""
BaseModel module for AirBnB clone project.
"""
from datetime import datetime
import uuid

class BaseModel:
    """
    The BaseModel class for handling initialization, serialization, and deserialization.
    """
    def __init__(self):
        """
        Initialization logic here.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        String representation logic here.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Save logic here.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        To_dict logic here.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
