from homestorage import db, bcrypt
from homestorage.models import Item, User

db.create_all()

admin_username = "admin"
admin_password = "admin"
admin_password_hashed = bcrypt.generate_password_hash(admin_password).decode('utf-8')

admin = User(admin_username, admin_hashed_password)

db.session.add(admin)
db.session.commit()