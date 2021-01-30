from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hola')
def hola():
    return '<h1>Hola Mundo!!!</h1>'

@app.route('/user/<string:nombre>')
def regresarParam(nombre):
    return '<h1>Hola usuario: '+nombre+'</h1>'

@app.route('/num/<int:n>')
def regresarNum(n):
    return '<h1>Ingresaste el numero: {}</h1>'.format(n)

@app.route('/suma/<float:n1>/<float:n2>')
def regresarSum(n1,n2):
    res = n1+n2
    return '<h1>La suma de {} + {} = {}</h1>'.format(n1,n2,res)

if __name__ == '__main__':
    app.run()