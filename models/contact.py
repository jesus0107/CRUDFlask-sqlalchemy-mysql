from utils.db import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    phone = db.Column(db.String(30))

    def __init__(self, full_name, email, phone):
        self.full_name = full_name
        self.email = email
        self.phone = phone