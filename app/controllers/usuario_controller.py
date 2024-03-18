from flask import Blueprint, render_template, request, redirect, url_for
from models.Usuario import Usuario

usuario_bp = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_bp.route('/')
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuario/listar.html', usuarios=usuarios)

@usuario_bp.route('/crear', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        nuevo_usuario = Usuario(nombre=nombre, correo=correo)
        nuevo_usuario.guardar()
        return redirect(url_for('usuario.listar_usuarios'))
    return render_template('usuario/crear.html')

@usuario_bp.route('/actualizar/<int:id>', methods=['GET', 'POST'])
def actualizar_usuario(id):
    usuario = Usuario.query.get(id)
    if request.method == 'POST':
        usuario.nombre = request.form['nombre']
        usuario.correo = request.form['correo']
        usuario.actualizar()
        return redirect(url_for('usuario.listar_usuarios'))
    return render_template('usuario/actualizar.html', usuario=usuario)

@usuario_bp.route('/borrar/<int:id>', methods=['GET', 'POST'])
def borrar_usuario(id):
    usuario = Usuario.query.get(id)
    if request.method == 'POST':
        usuario.eliminar()
        return redirect(url_for('usuario.listar_usuarios'))
    return render_template('usuario/borrar.html', usuario=usuario)
