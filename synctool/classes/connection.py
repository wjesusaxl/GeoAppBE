import os, json
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from django.conf import settings

class Connection:
    securityConf = {}
    session = cluster = None

    def __init__(self):
        self.securityConf = self.GetConfigFile("synctool/dataStax")
        authProvider = PlainTextAuthProvider(self.securityConf["clientId"], self.securityConf["clientSecret"])
        cloudConfig = {
            "secure_connect_bundle": self.securityConf["secureConnectBundle"]
        }
        cluster = Cluster(cloud=cloudConfig, auth_provider=authProvider)
        self.session = cluster.connect()
        self.session.execute(f"use {self.securityConf['defaultDatabase']}")

    def getConfigFile(entry):    
        with open(os.path.join(settings.BASE_DIR, f"static/conf/{entry}.json")) as conf:
            conf = json.load(conf)    
        return conf

    def dropDataType(dataType, ifExists=True):
        result = {}

        return result

    def runCommand(cql):

        result = {}

        return result

    def returnData(cql):

        result = {}

        return result
        
