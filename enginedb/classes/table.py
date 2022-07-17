import os, json
from django.conf import settings

from enginedb.classes.dbobject import DBObject

class Table(DBObject):
    objectType="table"
    def __init__(self, keyspace):
        super().__init__(keyspace=keyspace)        
 
    def drop(self, name):        
        return super().callDmlApi(
            objectType=self.objectType,
            action="drop",
            body=None,
            params={'name':name}
        )       

    def create(self, object):
        return super().callDmlApi(
            objectType=self.objectType,
            action="create",
            body=self.__addDBOptions(object)
        )

    def __addDBOptions(self, object):
        if not "tableOptions" in object:
            object["tableOptions"] = {
                "defaultTimeToLive" : 0
            }
        object["ifNotExists"] = True
        return object

    