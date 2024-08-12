from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
import urllib.parse

load_dotenv()


# MongoDB connection details
username = os.getenv("MONGO_DB_USERNAME")
password = os.getenv("MONGO_DB_PASSWORD")
cluster_name = os.getenv("MONGO_DB_CLUSTER_NAME")
database_name = os.getenv("MONGO_DB_DATABASE_NAME")

# Encode the username and password
encoded_username = urllib.parse.quote_plus(username)
encoded_password = urllib.parse.quote_plus(password)

# Construct the MongoDB URI with the encoded username and password
MONGO_URI = f"mongodb+srv://{encoded_username}:{encoded_password}@{cluster_name}.kz4mur9.mongodb.net/{database_name}?retryWrites=true&w=majority"
client = AsyncIOMotorClient(MONGO_URI)
db = client[database_name]



