from flask import Flask, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    if 'contador' not in session:
        session['contador'] = 0
    return 'Bienvenido!'

@app.route('/mostrar')
def mostrar():
    contador = session.get('contador', 0)
    return f'Has visitado esta página {contador} veces.'

@app.route('/incrementar_visitas_doble')
def incrementar_visitas_doble():
    session['contador'] = session.get('contador', 0) + 2
    return redirect(url_for('mostrar'))

@app.route('/reiniciar_visitas')
def reiniciar_visitas():
    session['contador'] = 0
    return redirect(url_for('mostrar'))

if __name__ == '__main__':
    app.run(debug=True)