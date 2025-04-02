from flask import render_template, request ,redirect
from flask_app import app  # Importamos la app de la carpeta flask_app

from flask_app.models.cursos import Curso, obtener_todos as obtener_todos_los_cursos, crear_curso, obtener_curso_por_id
from flask_app.models.estudiante import Estudiante, obtener_todos as obtener_todos_los_estudiantes, crear_estudiante

@app.route("/cursos", methods=["POST", "GET"])
def cursos():
    if request.method == "POST":
        if request.form["nombre"]:
            curso = Curso(id=None, nombre=request.form["nombre"], created_at=None, updated_at=None)
            crear_curso(curso)
            return redirect("/cursos")
        pass
    return render_template("cursos.html", cursos=obtener_todos_los_cursos())

@app.route("/estudiante", methods=["POST", "GET"])
def estudiante():
    if request.method == "POST":
        if request.form["nombre"] and request.form["apellido"] and request.form["edad"] and request.form["curso_id"]:
            
            estudiante = Estudiante(id=None, nombre=request.form["nombre"], apellido=request.form["apellido"], edad=request.form["edad"], curso_id=request.form["curso_id"], created_at=None, updated_at=None)
            crear_estudiante(estudiante)
            return redirect("/estudiante")
    return render_template("estudiante.html", cursos=obtener_todos_los_cursos())

@app.route("/curso/<int:curso_id>")
def estudiantes_en_cursos(curso_id):
    return render_template("cursos_estudiantes.html", curso=obtener_curso_por_id(curso_id),estudiantes=obtener_todos_los_estudiantes(curso_id))
