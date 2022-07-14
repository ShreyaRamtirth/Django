from pymongo import MongoClient
from firstPage.config import database
CONNECTION_STRING = database
client = MongoClient(CONNECTION_STRING)
stock = client['stockmarket']
user_collection = stock["User"]

def get_db_register(temp):
    dict = { "name": temp["name"], "email": temp['email'], "contact": temp['number'], "password": temp['password'], 'role': 'user' }
    if not user_collection.find_one({"email": temp['email']}):
        x = user_collection.insert_one(dict)
    else:
        return "User Already Exists!"
    if x:
        return "Registration Succesful"
    else:
        return "Registration Unsuccesful"

def get_db_login(temp):
    creds = user_collection.find_one({"email":temp["email"], "password": temp["password"]})
    if creds:
        if creds['role'] == 'admin':
            return 'admin'
    else:
        return "User not found! Please Register"
    return True
