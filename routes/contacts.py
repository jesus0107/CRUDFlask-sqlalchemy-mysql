from flask import Blueprint, render_template

contacts = Blueprint('contacts', __name__)

@contacts.route('/')
def index():
    return render_template('index.html')

@contacts.route('/new')
def add_contact():
    return "Saving a contact"

@contacts.route('/update')
def update_contact():
    return "Updateing contact"
    
@contacts.route('/delete')
def delete_contact():
    return "deleted contact"

@contacts.route('/about')
def about():
    return render_template('about.html')