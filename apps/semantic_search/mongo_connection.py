import pymongo
from pymongo.errors import ConnectionFailure
from decouple import config

def get_mongo_client():
    """
    Establishes and returns a MongoDB client connection.
    """
    connection_string = config("MONGODB_URI")
    print(f"Connecting to MongoDB with URI: {connection_string}")

    try:
        client = pymongo.MongoClient(connection_string, tls=True, tlsAllowInvalidCertificates=True)
        client.admin.command('ping')
        print("MongoDB connection successful!")
        return client

    except ConnectionFailure:
        print("MongoDB connection failed.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
