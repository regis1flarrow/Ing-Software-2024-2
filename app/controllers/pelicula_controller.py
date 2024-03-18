from flask import Blueprint, render_template, request, redirect, url_for
from models.Pelicula import Pelicula

pelicula_bp = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@pelicula_bp.route('/')
def listar_peliculas():
    peliculas = Pelicula.query.all()
    return render_template('pelicula/listar.html', peliculas=peliculas)

@pelicula_bp.route('/crear', methods=['GET', 'POST'])
def crear_pelicula():
    if request.method == 'POST':
        nombre = request.form['nombre']
        genero = request.form['genero']
        duracion = request.form['duracion']
        inventario = request.form['inventario']
        nueva_pelicula = Pelicula(nombre=nombre, genero=genero, duracion=duracion, inventario=inventario)
        nueva_pelicula.guardar()
        return redirect(url_for('pelicula.listar_peliculas'))
    return render_template('pelicula/crear.html')

@pelicula_bp.route('/actualizar/<int:id>', methods=['GET', 'POST'])
def actualizar_pelicula(id):
    pelicula = Pelicula.query.get(id)
    if request.method == 'POST':
        pelicula.nombre = request.form['nombre']
        pelicula.genero = request.form['genero']
        pelicula.duracion = request.form['duracion']
        pelicula.inventario = request.form['inventario']
        pelicula.actualizar()
        return redirect(url_for('pelicula.listar_peliculas'))
    return render_template('pelicula/actualizar.html', pelicula=pelicula)

@pelicula_bp.route('/borrar/<int:id>', methods=['GET', 'POST'])
def borrar_pelicula(id):
    pelicula = Pelicula.query.get(id)
    if request.method == 'POST':
        pelicula.eliminar()
        return redirect(url_for('pelicula.listar_peliculas'))
    return render_template('pelicula/borrar.html', pelicula=pelicula)
