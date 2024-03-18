from flask import Blueprint, render_template, request, redirect, url_for
from models.Rentar import Renta

renta_bp = Blueprint('renta', __name__, url_prefix='/renta')

@renta_bp.route('/')
def listar_rentas():
    rentas = Renta.query.all()
    return render_template('renta/listar.html', rentas=rentas)

@renta_bp.route('/crear', methods=['GET', 'POST'])
def crear_renta():
    if request.method == 'POST':
        id_usuario = request.form['id_usuario']
        id_pelicula = request.form['id_pelicula']
        nueva_renta = Renta(id_usuario=id_usuario, id_pelicula=id_pelicula)
        nueva_renta.guardar()
        return redirect(url_for('renta.listar_rentas'))
    return render_template('renta/crear.html')

@renta_bp.route('/actualizar/<int:id>', methods=['GET', 'POST'])
def actualizar_renta(id):
    renta = Renta.query.get(id)
    if request.method == 'POST':
        renta.entregada = True if request.form.get('entregada') else False
        renta.actualizar()
        return redirect(url_for('renta.listar_rentas'))
    return render_template('renta/actualizar.html', renta=renta)

@renta_bp.route('/borrar/<int:id>', methods=['GET', 'POST'])
def borrar_renta(id):
    renta = Renta.query.get(id)
    if request.method == 'POST':
        renta.eliminar()
        return redirect(url_for('renta.listar_rentas'))
    return render_template('renta/borrar.html', renta=renta)
