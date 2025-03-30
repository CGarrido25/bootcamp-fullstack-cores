from flask import Flask, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/reiniciar_visitas')
def reiniciar_visitas():
    session['contador'] = 0
    return redirect(url_for('mostrar'))