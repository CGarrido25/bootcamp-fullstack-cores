from flask_app.config.my_sql_conection import connectToMySQL
class Usuario:
    
    
    
    def __init__(self, id, nombre,apellido, email,created_at,updated_at):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at
        
    
    def __str__(self):
        return f"Usuario(id={self.id}, nombre='{self.nombre}', correo='{self.correo}')"


def obtener_todos():
    query= "SELECT * FROM usuario.usuarios;"
    usuarios_en_bd = connectToMySQL("usuario").query_db(query)
    usurios = []
    for usuario in usuarios_en_bd:
        usuario = Usuario(usuario["id"], usuario["nombre"],usuario["apellido"], usuario["email"], usuario["created_at"], usuario["updated_at"])
        usurios.append(usuario)
    return usurios


def crear_usuario(usuario:Usuario):
    query = "INSERT INTO usuario.usuarios (nombre, apellido, email, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());"
    data = {
        "nombre": usuario.nombre,
        "apellido": usuario.apellido,
        "email": usuario.email
    }
    return connectToMySQL("usuario").query_db(query, data)

def borrar_usuario(id):
    query = "DELETE FROM usuario.usuarios WHERE id = %(id)s;"
    data = {
        "id": id
    }
    return connectToMySQL("usuario").query_db(query, data)


def obtener_usuario_por_id(id):
    query = "SELECT * FROM usuario.usuarios WHERE id = %(id)s;"
    data = {
        "id": id
    }
    usuario_en_bd = connectToMySQL("usuario").query_db(query, data)
    if usuario_en_bd:
        usuario = Usuario(usuario_en_bd[0]["id"], usuario_en_bd[0]["nombre"],usuario_en_bd[0]["apellido"], usuario_en_bd[0]["email"], usuario_en_bd[0]["created_at"], usuario_en_bd[0]["updated_at"])
        return usuario
    else:
        return None
    
def actualizar_usuario(usuario:Usuario):
    query = "UPDATE usuario.usuarios SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
    data = {
        "id": usuario.id,
        "nombre": usuario.nombre,
        "apellido": usuario.apellido,
        "email": usuario.email
    }
    return connectToMySQL("usuario").query_db(query, data)    