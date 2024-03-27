from pymongo import MongoClient

uri = "mongodb+srv://noa:5KhdTwuy57OZjTVj@cluster0.ij9y3ap.mongodb.net"

# Connect to the MongoDB cluster
client = MongoClient(uri)

# Access the database
db = client.finalProject