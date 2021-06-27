import pyrebase
import time
from main import main

config = {
    "apiKey": "AIzaSyA5N8XLwOPOZSoq3wYjCi9LMxZN0yc3Am0",
    "authDomain": "pridehacks.firebaseapp.com",
    "databaseURL": "https://pridehacks-default-rtdb.firebaseio.com",
    "projectId": "pridehacks",
    "storageBucket": "pridehacks.appspot.com",
    "messagingSenderId": "1000942839264",
    "appId": "1:1000942839264:web:3ba5691cbe8e0aa496f785"
  }
firebase = pyrebase.initialize_app(config)
db = firebase.database()

def stream_handler(message):
    data = db.child('data').get().val()
    key = str(list(data.keys())[-1])
    path = main(dict(data[key])) # {'title': 'Pyrebase', "body": "etc..."}
    data[key]['download'] = path
    print(data[key])
    db.child('data').child(key).set(data[key])

my_stream = db.child("data").stream(stream_handler)
