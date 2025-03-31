from flask import Flask, render_template  

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/lista_paises')          
def lista_paises():
    
    paises = [
   {'pais': 'Argentina' , 'capital': 'Buenos Aires'},
   {'pais': 'Brasil' , 'capital': 'Brasilia'},
   {'pais': 'Chile' , 'capital': 'Santiago de Chile'},
   {'pais': 'Colombia' , 'capital': 'Bogotá'},
   {'pais': 'Costa Rica' , 'capital': 'San José'},
   {'pais': 'Paraguay' , 'capital': 'Asunción'},
   {'pais': 'Perú' , 'capital': 'Lima'}
    ]
    return render_template('index.html', lista_paises=paises)    # Renderiza la plantilla "index.html" y la devuelve como respuesta  





if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente   

   app.run(debug=True)    # Ejecuta la aplicación en modo de depuración/debug para detectar cualquier cambio y recargarlo