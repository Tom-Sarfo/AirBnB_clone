#!/usr/bin/python3
import uuid
from datetime import datetime
import models
"""A base model class representing common attributes and methods for other classes."""

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize a new instance of the BaseModel class."""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            models.storage.save()

    def __str__(self):
        """Return a string representation of the object."""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the 'updated_at' attribute with the current datetime."""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """create a dictionary representation
            suitable for serialization/deserialization
         """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

