from flask import Blueprint

contacts = Blueprint('contacts', __name__)

@contacts.route('/')
def index():
    return 'Hello'

@contacts.route('/contacts')
def get_contacts():
    return "contacts list"