#!/usr/bin/python3
"""Base model for airbnb """

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
        Base model that contains attribute common
        to all classes
    """
    def __init__(self, *args, **kwargs):
        """
            *args:
                parameter is included to capture any
                additional positional arguments
                that may be passed to the constructor.
                However, in this case, it won't be used.
            *kwargs:
                It allows us to pass a dictionary
                representation of an instance.
        """
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
            string that returns information about
            a classs
        """
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
            public instance method that updates the
            updated_at to the with the current date and time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values of
            _dict__ of the instance:
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
