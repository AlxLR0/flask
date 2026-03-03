from flask import Flask, render_template
from cliente_dao import ClienteDAO

app = Flask(__name__)

titulo_app = "Zona fit"

@app.route('/')
@app.route('/index.html')# url http://localhost:5000/index.html
def inicio():
    
    #recuperar los clientes de la bd
    clientes_db = ClienteDAO.seleccionar()

    
    return render_template('index.html', titulo=titulo_app, clientes= clientes_db) # render_template es una función que se encarga de renderizar una plantilla html, en este caso index.html, y le pasa el título de la aplicación como variable titulo
if __name__ == '__main__':
    app.run(debug=True)