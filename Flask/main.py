from flask import Flask, render_template, request, redirect, url_for, Response
from flask_sqlalchemy import SQLAlchemy
from typing import List

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Contactos.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

#si todo sigue sin andar se recomienda borrar toda la base de datos crear otra con otro nombre (recomendacion)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)


with app.app_context():
    db.create_all()  

@app.route('/')
def index() -> str:
    Contacts: List[Contact] = Contact.query.all() 
    return render_template('index.html', contacto=Contacts)

@app.route('/add', methods=['POST'])
def add_Contact():
    name: str = request.form['name']
    email: str = request.form['email']
    print(f"Nombre: {name}, Email: {email}")
    
    try:
        new_contact: Contact = Contact(name=name, email=email)
        db.session.add(new_contact)
        db.session.commit()
        print("Contacto agregado exitosamente.") #los print son solo para ver en consola y ver que es lo que esta mal (borrar este mensaje despues de leer)
    except Exception as e:
        db.session.rollback()  
        print(f"Error al guardar el contacto: {e}")


    return redirect(url_for('index'))

@app.route('/registrate', methods=['GET', 'POST'])
def registrate():
    return render_template('registrate.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    return render_template('contacto.html')

@app.route('/restaurant', methods=['GET', 'POST'])
def restaurant():
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