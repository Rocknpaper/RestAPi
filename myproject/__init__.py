from flask import Flask
from flask_mongoengine import MongoEngine
 

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    "db": "Project",
    "host": "13.233.236.4",
    "port": 27017
}

db = MongoEngine(app)




from myproject.RestApi.userApi import UserApi