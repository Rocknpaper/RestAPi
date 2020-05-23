from werkzeug.security import check_password_hash
from myproject import db

class User(db.Document):
    _id = db.StringField(primary_key=True, min_length=8, max_legth=8)
    username = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True)
    password = db.BinaryField(required=True)

    def checkPassword(self, password):
        return check_password_hash(self.password, password)

