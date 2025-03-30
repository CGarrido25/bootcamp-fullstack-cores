from flask import Flask, render_template, request, redirect, session #Agregamos sesión

app = Flask(__name__)

app.secret_key = '1234' #Establecemos una clave secreta


@app.route('/mostrar_usuario')
def mostrar_usuario():
   print("Usuario redirigido")
   print(request.form)  
   if session.get("nombre_usuario") is None or session.get("email_usuario") is None:
       return redirect('/crear_usuario')  
   if 'contador_visitas' not in session:
       session['contador_visitas'] = 0
   session['contador_visitas'] += 1

   return render_template("mostrar.html", contador=session['contador_visitas'])

@app.route('/incrementar_visitas')
def incrementar_visitas():
   if 'contador_visitas' not in session:
       session['contador_visitas'] = 0
   session['contador_visitas'] += 1
   return redirect('/mostrar_usuario')

@app.route('/incrementar_visitas_doble')
def incrementar_visitas_doble():
   if 'contador_visitas' not in session:
       session['contador_visitas'] = 0
   session['contador_visitas'] += 2
   return redirect('/mostrar_usuario')

@app.route('/index.html')
def index():
   return render_template('index.html') 

@app.route('/crear_usuario', methods=['POST', 'GET'])
def crear_usuario():
   if request.method == 'GET':
       return render_template('crear_usuario.html')
   else:
       return crear_usuario_post()
   
@app.route('/reiniciar_visitas')
def reiniciar_visitas():
    session['contador_visitas'] = 0
    return redirect('/mostrar_usuario')

def crear_usuario_post():
   print("Recibiendo información")
   print(request.form)
   if 'nombre' not in request.form or 'email' not in request.form:
       return "Faltan datos en el formulario", 400
   session['nombre_usuario'] = request.form['nombre']
   session['email_usuario'] = request.form['email']
   return redirect('/index.html')

@app.route('/destruir_sesion')
def destruir_sesion():
   session.clear()
   return redirect('/index.html')

if __name__ == "__main__": 
    app.run(debug=True)