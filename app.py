from flask import Flask
from flask import jsonify
from flask import request
import pymysql
import pymysql.cursors
from objects import generarCodigo
from objects import contacto

app = Flask(__name__)

#(1) Se van a importar datos desde el formulario hasta la base de datos

@app.route("/registro", methods=['GET','POST'])
def recording():
    data = request.form
    print (data)
    orientacion = data.get('orientacion')
    medidas = data.get('medidas')
    codigo = generarCodigo(orientacion,medidas)
    registro = 

#(3) Se corre el programa en el servidor
if __name__ == '__main__':
    app.run(debug=True)
   