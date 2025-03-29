from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación
from flask import render_template
from random import sample
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

cartas = [
        "1 El Gallo", "2 El Diablito", "3 La Dama", "4 El catrín",
        "5 El paraguas", "6 La sirena", "7 La escalera", "8 La botella",
        "9 El barril", "10 El árbol", "11 El melón", "12 El valiente",
        "13 El gorrito", "14 La muerte", "15 La pera", "16 La bandera",
        "17 El bandolón", "18 El violoncello", "19 La garza", "20 El pájaro",
        "21 La mano", "22 La bota", "23 La luna", "24 El cotorro",
        "25 El borracho", "26 El negrito", "27 El corazón", "28 La sandía",
        "29 El tambor", "30 El camarón", "31 Las jaras", "32 El músico",
        "33 La araña", "34 El soldado", "35 La estrella", "36 El cazo",
        "37 El mundo", "38 El apache", "39 El nopal", "40 El alacrán",
        "41 La rosa", "42 La calavera", "43 La campana", "44 El cantarito",
        "45 El venado", "46 El sol", "47 La corona", "48 La chalupa",
        "49 El pino", "50 El pescado", "51 La palma", "52 La maceta",
        "53 El arpa", "54 La rana"
    ]
 
@app.route('/loteria')  # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def loteria():
    muestra = sample(cartas, 16)
    return render_template('index.html', x=4, y=4,muestra=muestra)  # Devuelve el contenido de la plantilla "index.html" con los parámetros "x" y "y"


@app.route('/loteria/<int:x>')  # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def loteria_x(x):
    muestra = sample(cartas, 4*x)
    return render_template('index.html', x=x, y=4,muestra=muestra)  # Devuelve el contenido de la plantilla "index.html" con los parámetros "x" y "y"


@app.route('/loteria/<int:x>/<int:y>')  # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def loteria_x_y(x, y):
    muestra = sample(cartas, x*y)
    return render_template('index.html', x=x, y=y,muestra=muestra)  # Devuelve el contenido de la plantilla "index.html" con los parámetros "x" y "y"

if __name__ == "__main__":  # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente
    app.run(debug=True)  # Ejecuta la aplicación en modo de depuración/debug para detectar cualquier cambio y recargarlo