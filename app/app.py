from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models.Usuario import Usuario
from models.Pelicula import Pelicula
from models.Rentar import Renta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ferfong:Developer123!@localhost/lab_ing_software'
db = SQLAlchemy(app)

# Rutas para Usuario
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuario/listar.html', usuarios=usuarios)

@app.route('/usuarios/crear', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        nuevo_usuario = Usuario(nombre=request.form['nombre'], correo=request.form['correo'])
        db.session.add(nuevo_usuario)
        db.session.commit()
        return redirect(url_for('listar_usuarios'))
    return render_template('usuario/crear.html')

# Rutas para Película
@app.route('/peliculas', methods=['GET'])
def listar_peliculas():
    peliculas = Pelicula.query.all()
    return render_template('pelicula/listar.html', peliculas=peliculas)

@app.route('/peliculas/crear', methods=['GET', 'POST'])
def crear_pelicula():
    if request.method == 'POST':
        nueva_pelicula = Pelicula(nombre=request.form['nombre'], genero=request.form['genero'],
                                  duracion=request.form['duracion'], inventario=request.form['inventario'])
        db.session.add(nueva_pelicula)
        db.session.commit()
        return redirect(url_for('listar_peliculas'))
    return render_template('pelicula/crear.html')

# Rutas para Renta
@app.route('/rentas', methods=['GET'])
def listar_rentas():
    rentas = Renta.query.all()
    return render_template('renta/listar.html', rentas=rentas)

@app.route('/rentas/crear', methods=['GET', 'POST'])
def crear_renta():
    if request.method == 'POST':
        nueva_renta = Renta(idUsuario=request.form['idUsuario'], idPelicula=request.form['idPelicula'],
                            fecha_renta=request.form['fecha_renta'], dias_de_renta=request.form['dias_de_renta'])
        db.session.add(nueva_renta)
        db.session.commit()
        return redirect(url_for('listar_rentas'))
    return render_template('renta/crear.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
