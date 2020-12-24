from homestorage import db, ma, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    box = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(20), nullable=False, default="default.jpg")
    withdrawed = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self,  title, box, image="default.jpg", withdrawed=False):
        self.title = title
        self.box = box
        self.image = image
        self.withdrawed = withdrawed

class ItemSchema(ma.Schema):
  class Meta:
    fields = ("id", "title", "box", "image", "withdrawed")

