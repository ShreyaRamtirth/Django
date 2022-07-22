from unicodedata import name
import jwt
from pymongo import MongoClient
from firstPage.config import database
from django.http import HttpResponse  
CONNECTION_STRING = database
client = MongoClient(CONNECTION_STRING)
stock = client['stockmarket']
user_collection = stock["User"]
stock_collection = stock["Stock"]

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
            return ('admin',creds['name'])
    else:
        return ("User not found! Please Register")
    return ('user', creds['name'])


def getAllUsers(search):
    result = user_collection.find({})
    print(search)
    if search != None:
        result = user_collection.find({ 'name' : search})
    return result


def add_search(search,user):
    result = user_collection.find({ 'email' : user['Username']})
    dict = { "user": result[0]['_id'], "symbol": search}
    stock_collection.insert_one(dict)