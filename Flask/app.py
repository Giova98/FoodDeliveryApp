from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta'  # Necesario para los mensajes flash
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contactos.db'  # Base de datos en SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de Contacto
class Contacto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(15), nullable=True)
    motivo = db.Column(db.String(50), nullable=False)
    mensaje = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Contacto {self.nombre}>"

# Crear todas las tablas en la base de datos dentro del contexto de la app
with app.app_context():
    db.create_all()

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            nombre = request.form['nombre']
            email = request.form['email']
            telefono = request.form.get('telefono')  # Opcional
            motivo = request.form['motivo']
            mensaje = request.form['mensaje']

            # Crear una nueva instancia de Contacto
            nuevo_contacto = Contacto(
                nombre=nombre,
                email=email,
                telefono=telefono,
                motivo=motivo,
                mensaje=mensaje
            )

            # Agregar y guardar en la base de datos
            db.session.add(nuevo_contacto)
            db.session.commit()

            # Mensaje de confirmación para el usuario
            flash('Mensaje enviado con éxito', 'success')
            return redirect(url_for('index'))  # Redirigir a la página de inicio o a otra página

        except Exception as e:
            db.session.rollback()  # Revertir los cambios si ocurre un error
            flash('Error al enviar el mensaje. Intenta nuevamente.', 'error')
            return redirect(url_for('contacto'))  # Redirigir nuevamente a la página de contacto

    return render_template('contacto.html')

@app.route('/registrate')
def registrate():
    return render_template('registrate.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/restaurant')
def restaurant():
    return render_template('restaurant.html')  # Asegúrate de tener la plantilla 'restaurant.html' creada

@app.route('/helado')
def helado():
    return render_template('helado.html')  # Asegúrate de tener la plantilla 'helado.html' creada

@app.route('/cafeDely')
def cafeDely():
    return render_template('cafeDely.html')  # Asegúrate de tener la plantilla 'cafeDely.html' creada

@app.route('/tiendas')
def tiendas():
    return render_template('tiendas.html')  # Asegúrate de tener la plantilla 'tiendas.html' creada



if __name__ == '__main__':
    app.run(debug=True)

