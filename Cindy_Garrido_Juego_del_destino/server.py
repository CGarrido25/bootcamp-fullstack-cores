from flask import Flask, render_template, request, redirect, session #Agregamos sesión

app = Flask(__name__)

app.secret_key = '1234' #Establecemos una clave secreta


@app.route('/')
def index():
   return render_template("/index.html")

@app.route('/formulario', methods=['POST'])
def formulario():
    print("**********")
    print(request.form)
    session['nombre'] = request.form['nombre']
    session['lugar'] = request.form['lugar']
    session['numero'] = request.form['numero']
    session['comida'] = request.form['comida']
    print("**********")
    print(session)
    print("**********")
    return redirect("/ver_destino")


@app.route('/ver_destino')
def ver_destino():
    return render_template("/ver_destino.html",nombre=session['nombre'], lugar=session['lugar'], numero=session['numero'], comida=session['comida'])



if __name__ == "__main__": 
    app.run(debug=True)