from flask import Flask, redirect, render_template, url_for
from cliente import Cliente
from cliente_dao import ClienteDAO
from cliente_forma import ClienteForma

app = Flask(__name__)

app.config['SECRET_KEY'] = 'clave_secreta'

titulo_app = "Zona fit"

@app.route('/')
@app.route('/index.html')# url http://localhost:5000/index.html
def inicio():
    
    #recuperar los clientes de la bd
    clientes_db = ClienteDAO.seleccionar()

    #crear un objeto de cliente form vacio
    cliente = Cliente()
    cliente_form = ClienteForma(obj=cliente)

    
    return render_template('index.html', titulo=titulo_app, clientes= clientes_db, forma=cliente_form) # render_template es una función que se encarga de renderizar una plantilla html, en este caso index.html, y le pasa el título de la aplicación como variable titulo


@app.route('/guardar', methods=['POST'])
def guardar():
    #recuperar los clientes de la bd
    cliente = Cliente()
    cliente_form = ClienteForma(obj=cliente)
    if cliente_form.validate_on_submit(): # validate_on_submit es una función que se encarga de validar el formulario, si el formulario es válido, entonces se ejecuta el código dentro del if
        cliente_form.populate_obj(cliente) # populate_obj es una función que se encarga de llenar el objeto cliente con los datos del formulario, es decir, asigna los valores de los campos del formulario a los atributos del objeto cliente
        if not cliente.id:
            ClienteDAO.insertar(cliente) # insertar es una función que se encarga de insertar un cliente en la base de datos, recibe como parámetro el objeto cliente que se quiere insertar
        else:
            ClienteDAO.actualizar(cliente) # actualizar es una función que se encarga de actualizar un cliente en la base de datos, recibe como parámetro el objeto cliente que se quiere actualizar
    return redirect(url_for('inicio')) # redirect es una función que se encarga de redirigir a otra ruta, en este caso a la ruta de inicio


@app.route('/limpiar')
def limpiar():
    return redirect(url_for('inicio')) # se usa redirect para redirigir a la ruta de inicio, esto hace que se limpie el formulario y se muestren los clientes actualizados en la tabla

@app.route('/editar/<int:id>')
def editar(id):
    # obtener el cliente de la base de datos mediante su id
    cliente = ClienteDAO.seleccionar_por_id(id)
    # cargar los datos en el formulario para que se muestren en la interfaz
    cliente_form = ClienteForma(obj=cliente)
    # también mostrar la lista completa de clientes en la tabla
    clientes_db = ClienteDAO.seleccionar()
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db, forma=cliente_form) # se renderiza la plantilla index.html con el título de la aplicación, la lista de clientes actualizada y el formulario con los datos del cliente seleccionado


@app.route('/eliminar/<int:id>')
def eliminar(id):
    # construir un cliente con el id para pasarlo al DAO
    cliente = Cliente(id=id)
    ClienteDAO.eliminar(cliente)
    return redirect(url_for('inicio'))


if __name__ == '__main__':
    app.run(debug=True)