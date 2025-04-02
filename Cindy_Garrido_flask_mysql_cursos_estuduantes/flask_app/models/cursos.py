from flask_app.config.my_sql_conection import connectToMySQL

class Curso:
    def __init__(self, id, nombre,created_at,updated_at ):
        self.id = id
        self.nombre = nombre
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"Curso(id={self.id}, nombre='{self.nombre}', created_at='{self.created_at}', updated_at='{self.updated_at}')"
    
def obtener_todos():
    query= "SELECT * FROM esquema_estudiantes_cursos.cursos;"
    cursos_en_bd = connectToMySQL("esquema_estudiantes_cursos").query_db(query)
    cursos=[]
    for curso in cursos_en_bd:
        curso = Curso(curso["id"], curso["nombre"],curso["created_at"], curso["updated_at"])
        cursos.append(curso)
    return cursos

def crear_curso(curso:Curso):
    query = "INSERT INTO esquema_estudiantes_cursos.cursos (nombre, created_at, updated_at) VALUES (%(nombre)s, NOW(), NOW());"
    data = {
        "nombre": curso.nombre,
    }
    return connectToMySQL("esquema_estudiantes_cursos").query_db(query, data)

def obtener_curso_por_id(id):
    query = "SELECT * FROM esquema_estudiantes_cursos.cursos WHERE id = %(id)s;"
    data = {
        "id": int(id)
    }
    curso_en_bd = connectToMySQL("esquema_estudiantes_cursos").query_db(query, data)
    if curso_en_bd:
        curso = Curso(curso_en_bd[0]["id"], curso_en_bd[0]["nombre"],curso_en_bd[0]["created_at"], curso_en_bd[0]["updated_at"])
        return curso
    else:
        return None