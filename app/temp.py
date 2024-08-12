from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import urllib.parse
from .. import settings

MONGO_DB = {
    "username": "career525mentor",
    "password": "Mentor@1010",
    "cluster_name": "mentrentcluster1",
    "database_name": "ignitedminds"
}

# MongoDB connection details
username = MONGO_DB["username"]
password = MONGO_DB["password"]
cluster_name = MONGO_DB["cluster_name"]
database_name = MONGO_DB["database_name"]

# Encode the username and password
encoded_username = urllib.parse.quote_plus(username)
encoded_password = urllib.parse.quote_plus(password)

# Construct the MongoDB URI with the encoded username and password
uri = f"mongodb+srv://{encoded_username}:{encoded_password}@{cluster_name}.kz4mur9.mongodb.net/{database_name}?retryWrites=true&w=majority"




# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client[database_name]
