from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo para almacenar los datos de contacto
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=True)
    motivo = db.Column(db.String(50), nullable=False)
    mensaje = db.Column(db.Text, nullable=False)

# Crear la base de datos
with app.app_context():
    db.create_all()

# Ruta para mostrar el formulario de contacto y procesar el envío
@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form.get('telefono')
        motivo = request.form['motivo']
        mensaje = request.form['mensaje']

        # Crear un nuevo cliente y agregarlo a la base de datos
        nuevo_cliente = Cliente(nombre=nombre, email=email, telefono=telefono, motivo=motivo, mensaje=mensaje)
        db.session.add(nuevo_cliente)
        db.session.commit()

        # Mostrar en consola los datos enviados
        print(f"Nombre: {nombre}, Email: {email}, Teléfono: {telefono}, Motivo: {motivo}, Mensaje: {mensaje}")

        return redirect(url_for('contacto'))  # Redirige después de enviar el formulario

    return render_template('contacto.html')

# Ruta para ver la lista de clientes en una página especial
@app.route('/clientes')
def clientes():
    # Obtener todos los clientes desde la base de datos
    clientes = Cliente.query.all()
    return render_template('clientes.html', clientes=clientes)

if __name__ == '__main__':
    app.run(debug=True)
