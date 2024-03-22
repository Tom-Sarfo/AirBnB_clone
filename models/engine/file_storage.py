#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(objdict, file)

    def reload(self):
        """Deserialize object from json file to dictionary object"""
        try:
            with open(self.__file_path) as file:
                file_chunk = file.read()
                if file_chunk:
                    objdict = json.load(file_chunk)
                    for _key,_obj in objdict.items():
                        _class_name, _objId = _key.split('.')
                        _obj["created_at"] = datetime.strptime(_obj["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                        _obj["updated_at"] = datetime.strptime(_obj["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                        class_def = globals()[_class_name]
                        objct = class_def(**_obj)
                        self._objects[key] = objct
                    
                    self.new(eval(cls_name)(**_obj))
        except FileNotFoundError:
            return
