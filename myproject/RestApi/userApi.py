from flask_restful import Resource, Api
from werkzeug.security import generate_password_hash
from flask import request
import base64
from myproject.models.user import User
from myproject import app

class UserApi(Resource):
    def post(self):
        body = request.get_json()
        body["password"] = body["password"].encode()
        try:
            User(**body).save()
            return {"Status": "OK"}

        except Exception as e:
            return {"Status": "Failed", "Exception": str(e)}

api = Api(app)

api.add_resource(UserApi, "/users")
    
        
