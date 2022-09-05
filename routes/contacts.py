from crypt import methods
from flask import Blueprint, render_template, request, redirect,url_for
from utils.db import db
from models.contact import Contact

contacts = Blueprint('contacts', __name__)

@contacts.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts = contacts)

@contacts.route('/new', methods=['POST'])
def add_contact():
    full_name = request.form['full_name']
    email = request.form['email']
    phone = request.form['phone']
    new_contact = Contact(full_name, email, phone)

    db.session.add(new_contact)
    db.session.commit()
    return redirect(url_for('contacts.index'))

@contacts.route('/update/<id>', methods=['POST', 'GET'])
def update_contact(id):
    contact = Contact.query.get(id)
    if request.method == 'POST':
        contact.full_name = request.form['full_name']
        contact.email = request.form['email']
        contact.phone = request.form['phone']
        db.session.commit()
        return redirect(url_for('contacts.index'))
    
    return render_template('update.html', contact=contact)
    
@contacts.route('/delete/<id>')
def delete_contact(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('contacts.index'))

@contacts.route('/about')
def about():
    return render_template('about.html')