from flask import Flask, render_template
from flask import request

app=Flask(__name__)

@app.route('/')
def index():
    nombre = 'Yo'
    lista = ['uno','dos','tres','cuatro']
    return render_template('index.html',nombre=nombre,lista=lista)

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

@app.route('/materia')
def indexMateria():
    return render_template('materias.html')

@app.route('/suma',methods=['GET','POST'])
def suma():
    if request.method== 'POST':
        num1 = request.form.get('n1')
        num2 = request.form.get('n2')
        return '<h2>la suma es: {}</h2>'.format(str(int(num1)+int(num2)))
    else:
        return '''<form action="/suma" method="POST">
                    <label>Numero 1:</label>
                    <input class="form-control" type="text" name="n1"><br><br>
                    <label>Numero 2:</label>
                    <input class="form-control" type="text" name="n2"><br><br>
                    <button class="btn btn-primary">Calcular</button>
                </form>'''

@app.route('/operaciones',methods=['GET','POST'])
def ejeOpe():
   
   return render_template('operaciones.html')

@app.route('/resultado',methods=['GET','POST'])
def hacerOpe():
    num1 = request.form.get('n1')
    num2 = request.form.get('n2')
    res = int(num1) * int(num2) 
    return render_template('resultado.html',res=res,num1=num1,num2=num2)

if __name__ == '__main__':
    app.run()