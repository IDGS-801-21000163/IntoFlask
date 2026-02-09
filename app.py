import math
import os

from flask import Flask, render_template, request, flash
from flask_wtf.csrf import CSRFProtect

from forms import UserForm

app = Flask(__name__)
app.secret_key = 'clavesita secretita'
csrf = CSRFProtect()

@app.route('/')
def index():
    titulo = "Flask IDGS801"
    lista=["Juan", "Mario", "Pedro", "Dario"]
    return render_template('index.html', titulo=titulo, lista=lista)

@app.route('/alumnos')
def alumnos():
    return render_template('alumnos.html')

@app.route('/usuarios', methods=["GET", "POST"])
def usuarios():
    usuario = {
        'matricula': None,
        'nombre': None,
        'apellido_uno': None,
        'apellido_dos': None,
        'correo': None
    }

    clase = UserForm(request.form)
    if request.method == 'POST' and clase.validate():
        usuario['matricula'] = clase.matricula.data
        usuario['nombre'] = clase.nombre.data
        usuario['apellido_uno'] = clase.apellido_uno.data
        usuario['apellido_dos'] = clase.apellido_dos.data
        usuario['correo'] = clase.correo.data
        mensaje = 'Bienvenido {}'.format(usuario['nombre'])
        flash(mensaje)

    return render_template('usuarios.html', form=clase, usuario=usuario)

@app.route('/operasBas', methods=['POST', 'GET'])
def operasBas():
    n1=0
    n2=0
    res=0

    if request.method == 'POST':
        n1 = request.form['n1']
        n2 = request.form['n2']
        res=float(n1)+float(n2)

    return render_template('operasBas.html',n1=n1,n2=n2,res=res)

@app.route('/resultado', methods=['POST', 'GET'])
def resultado():
    n1 = request.form['n1']
    n2 = request.form['n2']

    temp = float(n1) + float(n2)

    return f"La suma es: {temp}"

@app.route('/hello')
def hello():
    return "Hello World"

@app.route('/user/<string:name>')
def hello_world(name):
    return "Hello " + name

@app.route('/numero/<int:numero>')
def numero(numero):
    return str(numero)

@app.route('/user/<int:id>/<string:username>')
def user(id, username):
    return str(id) + " " + username

@app.route('/suma/<float:numero1>/<float:numero2>')
def suma(numero1, numero2):
    return str(numero1 + numero2)

@app.route('/default')
@app.route('/default/<string:nombre>')
def default(nombre = 'Juan'):
    return nombre

@app.route('/operas')
def operas():
    return '''
        <form>
            <label for="name"></label>
            <input type="text" id="name" name="name" required>
            <br>
            <label for="name">apaterno:</label>
            <input type="text" id="name" name="name" required>
        </form>
    '''

@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    resultado = None

    if request.method == "POST":
        x1 = float(request.form["x1"])
        y1 = float(request.form["y1"])
        x2 = float(request.form["x2"])
        y2 = float(request.form["y2"])

        resultado = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return render_template("distancia/index.html", resultado=resultado)


@app.route("/cinepolis", methods=["GET", "POST"])
def cinepolis():
    total = None
    error = None

    if request.method == "POST":
        try:
            nombre = request.form["nombre"]
            compradores = int(request.form["compradores"])
            boletos = int(request.form["boletos"])
            tarjeta = request.form.get("tarjeta")

            if boletos > compradores * 7:
                error = "No se pueden comprar más de 7 boletos por persona"
            else:
                subtotal = boletos * 15
                descuento = 0

                if boletos > 5:
                    descuento += 0.15
                elif 3 <= boletos <= 5:
                    descuento += 0.10

                if tarjeta == "si":
                    descuento += 0.10

                total = subtotal - (subtotal * descuento)

        except:
            error = "Datos inválidos"

    return render_template("cinepolis/index.html", total=total, error=error)

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)