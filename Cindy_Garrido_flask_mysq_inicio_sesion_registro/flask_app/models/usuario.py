from flask_app.config.my_sql_conection import connectToMySQL

class Usuario:
    def __init__(self,  nombre, apellido, email,contrasena,id=None,created_at=None, updated_at=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contrasena = contrasena
        self.created_at = created_at
        self.updated_at = updated_at
    

    def __repr__(self):
        return f"Usuario(id={self.id}, nombre='{self.nombre}', apellido='{self.apellido}', email='{self.email}', created_at='{self.created_at}', updated_at='{self.updated_at}')"
    

def crear_usuario(usuario):
    query = "INSERT INTO esquema_usuarios.usuario (nombre, apellido, email, contrasena) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(contrasena)s);"
    print(usuario)
    data = {
        "nombre": usuario['nombre'],
        "apellido": usuario['apellido'],
        "email": usuario['email'],
        "contrasena": usuario['contrasena']
    }
    return connectToMySQL("esquema_usuarios").query_db(query, data)


def obtener_usuario_por_email(email):
    query = "SELECT * FROM esquema_usuarios.usuario WHERE email = %(email)s;"
    data = {
        "email": email
    }
    result = connectToMySQL("esquema_usuarios").query_db(query, data)
    if len(result) == 0:
        return False
    else:
        return Usuario(
            id=result[0]['id'],
            nombre=result[0]['nombre'],
            apellido=result[0]['apellido'],
            email=result[0]['email'],
            contrasena=result[0]['contrasena'],
            created_at=result[0]['created_at'],
            updated_at=result[0]['updated_at']
        )