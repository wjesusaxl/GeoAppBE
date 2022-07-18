import os, json, requests
from django.http import JsonResponse
# from cassandra.cluster import Cluster
# from cassandra.auth import PlainTextAuthProvider
from django.conf import settings

class apiRequestException(Exception):
    status_code = 400
    default_detail = 'Request does not fulfill required payload.'
    default_code = 'bad_request'

class Connection:
    securityConf = dbConnParams = {}
    # session = cluster = None
    keyspace = ""

    def __init__(self, keyspace=""):
        self.securityConf = self.__getConfigFile("synctool/dataStax")
        self.dbConnParams = self.__getConfigFile("api/database")        

        # print(os.path.join(settings.BASE_DIR, f"static/"))
        # authProvider = PlainTextAuthProvider(self.securityConf["clientId"], self.securityConf["clientSecret"])
        # cloudConfig = {
        #     "secure_connect_bundle": os.path.join(settings.BASE_DIR, f"static/") + self.securityConf["secureConnectBundle"]
        # }
        # print(cloudConfig)
        # cluster = Cluster(cloud=cloudConfig, auth_provider=authProvider)
        # self.session = cluster.connect()
        # self.keyspace = keyspace
        # self.session.execute(f"use {self.keyspace}")
        


    # def dropDataType(self, object, ifExists=True):

    #     if not ("name" in object or "keyspace" in object):
    #         raise apiRequestException

    #     params = {
    #         "keyspace": object["keyspace"],
    #         "name": object["name"]
    #     }
        
    #     return self.__callDmlApi("drop-type", body=None, params=params)       

        
    def __upsertData(self, keyspace, entity, data):
        geodb = self.dbConf['geodb']
        url = f"https://{geodb['dbID']}-{geodb['dbRegion']}.apps.astra.datastax.com/api/rest/v2/keyspaces/{keyspace}/{entity}"
        result = []

        for item in data:
            response = requests.post(url, json=item, headers={"x-cassandra-token": f"{geodb['dbApplicationToken']}"})
            status = response.status_code
            result.append( {
                "id": item["id"],
                "status": status,
                "response": json.loads(response.text)
            })

        return result

    def __updateData(self, keyspace, entity, data, id):
        geodb = self.dbConf['geodb']
        url = f"https://{geodb['dbID']}-{geodb['dbRegion']}.apps.astra.datastax.com/api/rest/v2/keyspaces/{keyspace}/{entity}/" + '/{id}'
        result = []

        for item in data:
            response = requests.put(url, json=item, headers={"x-cassandra-token": f"{geodb['dbApplicationToken']}"})
            status = response.status_code
            result.append( {
                "id": item["id"],
                "status": status,
                "response": json.loads(response.text)
            })

        return result

    def __getConfigFile(self, entry):    
        with open(os.path.join(settings.BASE_DIR, f"static/conf/{entry}.json")) as conf:
            conf = json.load(conf)
        
        return conf

    def __filterDataset(self, data, fields):
        dataset = []                
        for r in data:
            o = {}
            row = r["fields"]
            for f in fields:
                o[fields[f]] = row[f]
            dataset.append(o)
        return dataset