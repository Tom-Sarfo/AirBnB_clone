#!/usr/bin/python3
import uuid
from datetime import datetime
import models
"""A base model class representing common attributes and methods for other classes."""

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize a new instance of the BaseModel class."""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of the object."""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the 'updated_at' attribute with the current datetime."""

        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """create a dictionary representation
            suitable for serialization/deserialization
         """
        object_dict = self.__dict__.copy()
        object_dict['__class__'] = self.__class__.__name__
        object_dict['created_at'] = self.created_at.isoformat()
        object_dict['updated_at'] = self.updated_at.isoformat()
        return object_dict

