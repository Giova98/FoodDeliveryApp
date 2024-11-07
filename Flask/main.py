from flask import Flask, render_template, request, redirect, url_for, Response
from flask_sqlalchemy import SQLAlchemy
from typing import List, Any, Tuple

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Contactos.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Contact(db.Model):  # Aquí cambiamos 'db.model' a 'db.Model'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)


with app.app_context():
    db.create_all

@app.route('/')
def index() -> str:
 Contacts: list[tuple[any]] = Contact.query().all()

 return render_template('index.html', Contacts = Contacts)


@app.route('/add', method = ['POST'] )
def  add_Contact() -> Response :
   name: str = request.form['name']
   email: str = request.form['email']

   new_contact : Contact = Contact(name=name, email=email)
   db.session.add(new_contact)
   db.session.commit()

   return redirect(url_for('index'))


if __name__ == '__main__':
   app.run(debug=True)
