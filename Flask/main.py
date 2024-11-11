from flask import Flask, render_template, request, redirect, url_for, Response
from flask_sqlalchemy import SQLAlchemy
from typing import List, Any  # Usamos las importaciones correctas de tipos

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Contactos.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

# Se debe llamar la función con los paréntesis para crear las tablas
with app.app_context():
    db.create_all()  # Llamamos la función correctamente

@app.route('/')
def index() -> str:
    # Corregir el uso de la consulta
    Contacts: List[Contact] = Contact.query.all()  # Obtenemos todos los contactos
    return render_template('index.html', contacto=Contacts)



@app.route('/add', methods=['POST'])
def add_Contact() -> Response:
    name: str = request.form['name']
    email: str = request.form['email']

    if '@' not in email:  # Verificamos si el email tiene el símbolo @
     return render_template ('error.html')
    
    # Crear un nuevo objeto Contact y agregarlo a la base de datos
    new_contact: Contact = Contact(name=name, email=email)
    db.session.add(new_contact)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/delete/<int:id>') # Funcion eliminar id usuario
def delete_contact(id: int) -> Response:
    contact: Contact = Contact.query.get(id)
    
    if contact:
        db.session.delete(contacto)
        db.session.commit()
        
    return redirect(url_for('index'))

@app.route('/registrate', methods=['GET', 'POST'])
def registrate():
    # código de la vista
    return render_template('registrate.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    return render_template('contacto.html')

@app.route('/restaurant', methods=['GET', 'POST'])
def restaurant():
    # código de la vista
    return render_template('restaurant.html')

@app.route('/helado', methods=['GET', 'POST'])
def helado():
    return render_template('helado.html')
@app.route('/cafeDely', methods=['GET', 'POST'])
def cafeDely():
    
    return render_template('cafeDely.html')

@app.route('/tiendas', methods=['GET', 'POST'])
def tiendas():
    return render_template('tiendas.html')


if __name__ == '__main__':
    app.run(debug=True)
