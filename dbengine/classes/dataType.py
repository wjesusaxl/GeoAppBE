import os, json
from django.conf import settings

from .dbobject import DBObject

class DataType(DBObject):
    objectType = "dataType"
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
            body=object
        )

    def checkTypeIsUsed(self, name):
        api = """curl -s -L -X POST https://$ASTRA_CLUSTER_ID-$ASTRA_REGION.apps.astra.datastax.com/api/rest/v2/schemas/keyspaces/users_keyspace/tables/users/columns \
            -H "X-Cassandra-Token: $ASTRA_DB_APPLICATION_TOKEN" \
            -H  "Accept: application/json" \
            -H "Content-Type: application/json" \
            -d '{
            "name": "address",
            "typeDefinition": "address_type"
            }'"""


    