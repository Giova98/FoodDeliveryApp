from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = 'FoodDeliveyAppTP'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'murikawaii1234'
app.config['MYSQL_DB'] = 'Users'  
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        password = request.form.get('password')
        
        print(f"Datos recibidos: Nombre: {nombre}, Email: {email}, Password: {password}")
        
        hashed_password = generate_password_hash(password)
        
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO usuarios (nombre, email, user_password) VALUES (%s, %s, %s)',
                           (nombre, email, hashed_password))
            mysql.connection.commit()
            cursor.close()
            
            print("Registro exitoso en la base de datos")
            flash('Registro exitoso')
            return redirect(url_for('registro'))
        except Exception as e:
            print(f"Error al registrar: {str(e)}")
            flash(f'Error al registrar: {str(e)}')
    
    return render_template('registro.html')

if __name__ == '_main_':
    app.run(debug=True)