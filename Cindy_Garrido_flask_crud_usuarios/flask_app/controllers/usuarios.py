from flask import render_template, request ,redirect
from flask_app import app  # Importamos la app de la carpeta flask_app

from flask_app.models.usuario import Usuario,obtener_todos,crear_usuario,borrar_usuario, obtener_usuario_por_id, actualizar_usuario

@app.route("/usuarios")
def usuarios():
    usuarios = obtener_todos()  # Obtenemos todos los usuarios
    print(usuarios)  # Imprimimos los usuarios en la consola para depuración
    return render_template("usuario.html", usuarios=usuarios)


@app.route("/usuarios/nuevo", methods=["POST", "GET"])
def usuarios_nuevo():
    if request.method == "POST":
        usuario = Usuario(id=None,nombre=request.form["nombre"], apellido=request.form["apellido"], email=request.form["email"], created_at=None, updated_at=None)  # Creamos una instancia de Usuario con los datos del formulario
        crear_usuario(usuario)  # Llamamos a la función para crear un nuevo usuario
        return redirect("/usuarios")
    return render_template("crear_usuario.html")


@app.route("/usuarios/<int:id>/borrar")
def usuarios_borrar(id):
    borrar_usuario(id) 
    print(f"Usuario con ID {id} borrado.") 
    return redirect("/usuarios")

@app.route("/usuarios/<int:id>/ver")
def usuarios_ver(id):
    usuario = obtener_usuario_por_id(id)
    if usuario:
        return render_template("ver_usuario.html", usuario=usuario)
    else:
        return "Usuario no encontrado", 404
    
@app.route("/usuarios/<int:id>/editar", methods=["POST", "GET"])
def usuarios_editar(id):
    usuario = obtener_usuario_por_id(id)
    if usuario== None:
        return "Usuario no encontrado", 404
    
    if request.method == "GET":
        return render_template("editar_usuario.html", usuario=usuario)
    else:
        usuario = Usuario(id=id,nombre=request.form["nombre"], apellido=request.form["apellido"], email=request.form["email"], created_at=None, updated_at=None) 
        usuario_actualizado=actualizar_usuario(usuario)
        print(f"Usuario con ID {id} actualizado.")
        print(usuario_actualizado)
        return redirect("/usuarios")

    
    
    