from flask_app.config.my_sql_conection import connectToMySQL

class Estudiante:
    def __init__(self,  nombre, apellido, edad,id=None,created_at=None, updated_at=None,curso_id=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.created_at = created_at
        self.updated_at = updated_at
        self.curso_id = curso_id

    def __repr__(self):
        return f"Estudiante(id={self.id}, nombre='{self.nombre}', apellido='{self.apellido}', edad='{self.edad}', created_at='{self.created_at}', updated_at='{self.updated_at}')"
    
    
def obtener_todos(curso_id):
    query= "SELECT * FROM esquema_estudiantes_cursos.estudiantes WHERE curso_id =%(curso_id)s;"
    data = {
        "curso_id": int(curso_id)
    }
    estudiantes_en_bd = connectToMySQL("esquema_estudiantes_cursos").query_db(query, data)
    estudiantes=[]
    for estudiante in estudiantes_en_bd:
        estudiante = Estudiante(id=estudiante["id"], nombre=estudiante["nombre"],apellido=estudiante["apellido"], edad=estudiante["edad"], created_at=estudiante["created_at"], updated_at=estudiante["updated_at"])
        estudiantes.append(estudiante)
    return estudiantes

def crear_estudiante(estudiante:Estudiante):
    query = "INSERT INTO esquema_estudiantes_cursos.estudiantes (nombre, apellido, edad, curso_id, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(edad)s, %(curso_id)s, NOW(), NOW());"
    data = {
        "nombre": estudiante.nombre,
        "apellido": estudiante.apellido,
        "edad": int(estudiante.edad),
        "curso_id": int(estudiante.curso_id)
    }
    return connectToMySQL("esquema_estudiantes_cursos").query_db(query, data)
