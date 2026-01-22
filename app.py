from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

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

if __name__ == '__main__':
    app.run(debug=True)