from importlib.metadata import metadata
from .dataType import DataType
from .table import Table
from .metadata import Metadata
from operator import itemgetter

class Task:
    metadata = None
    def __init__(self):
        self.metadata = Metadata
    def process(self, objectType, action, objectName):        
        objects = self.dictToList(self.metadata.getObjects(objectType=objectType, objectName=objectName))
        if action == "create":
            objects = sorted(objects, key=itemgetter('creation_order'))
        if action == "drop":
            objects = sorted(objects, key=itemgetter('deletion_order'))
        result = {}        
        
        for o in objects:            
            if objectType=="datatype":                
                dt = DataType(o['keyspace'])
                if action == "drop":                    
                    result[o['code']]=dt.drop(o['name'])
                if action == "create":
                    result[o['code']]=dt.create(o)
        
            if objectType=="table":
                t = Table(o['keyspace'])
                if action == "drop":
                    result[o['code']]=t.drop(o['name'])
                if action == "create":
                    result[o['code']]=t.create(o)



        return result

    def dictToList(self, dict):
        result = []
        for k in list(dict):
            item = dict[k]
            if not "code" in dict:
                item["code"] = k
            result.append(item)
        return result

