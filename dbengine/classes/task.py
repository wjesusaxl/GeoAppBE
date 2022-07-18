from importlib.metadata import metadata
from .dataType import DataType
from .table import Table
from .metadata import Metadata

class Task:
    metadata = None
    def __init__(self):
        self.metadata = Metadata
    def Process(self, objectType, action, objectName):
        objects = self.metadata.getObjects(objectType=objectType, objectName=objectName)        
        result = {}        
        for o in objects.keys():
            if objectType=="datatype":                
                dt = DataType(objects[o]['keyspace'])
                if action == "drop":
                    result[o]=dt.drop(objects[o]['name'])
                if action == "create":
                    result[o]=dt.create(objects[o])
        
            if objectType=="table":
                t = Table(objects[o]['keyspace'])
                if action == "drop":
                    result[o]=t.drop(objects[o]['name'])
                if action == "create":
                    result[o]=t.create(objects[o])
        return result

    

