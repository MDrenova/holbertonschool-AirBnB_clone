from models.base_model import BaseModel
import json
import os
""" file storage """

class FileStorage:
    """ file storage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key_val = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key_val] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w") as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = {
                    k: BaseModel(**v) for k, v in json.load(f).items()
                }
        except FileNotFoundError:
            pass
