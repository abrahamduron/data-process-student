import pymongo
import os

class DbMongo:

    @staticmethod
    def getDB():
        user = os.environ['USERMONGO']
        password = os.environ['PASSWORDMONGO']
        cluster = os.environ['CLUSTER']
        query_string = 'retryWrites=true&w=majority'

        ## Connection String
        uri = "mongodb+srv://{0}:{1}@{2}/?{3}".format(
            user
            , password
            , cluster
            , query_string
        )

        client = pymongo.MongoClient(uri)
        db = client[os.environ['DB']]

        return client, db

    #mongodb+srv://abrjesus:<password>@cluster0.ntblok2.mongodb.net/?retryWrites=true&w=majority