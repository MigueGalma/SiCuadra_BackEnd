from flask import Flask
from flask import jsonify
from flask import request
import pymysql
import pymysql.cursors
from objects import generarCodigo
from objects import Consulta

app = Flask(__name__)

#(1) Se van a importar datos desde el formulario hasta la base de datos
"""
@app.route("/registro", methods=['GET','POST'])
def recording():
    data = request.form
    print (data)
    orientacion = data.get('orientacion')
    medidas = data.get('medidas')
    codigo = generarCodigo(orientacion,medidas)
    connection = pymysql.connect (host='localhost',
                                  user='root',
                                  password='',
                                  database='scdb',
                                  charset='utf8',
                                  cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            sql1 = "INSERT INTO `Registros` (`nombre`,`apellido`,`email`,`direccion`,`localidad`,`provincia`,`codigopostal`,`tematica`,`codigo`)\
                   VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql1,
                           (data['nombre'],
                           data['apellido'],
                           data['email'],
                           data['direccion'],
                           data['localidad'],
                           data['provincia'],
                           data['codigopostal'],
                           data['tematica'],
                           codigo))
            connection.commit()
    return data
"""

@app.route("/respuesta")
def answering():
    vector =[]
    connection = pymysql.connect (host='localhost',
                                  user='root',
                                  password='',
                                  database='scdb',
                                  charset='utf8',
                                  cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            sql2 = "select `idRegistros`, `nombre`, `apellido`, `tematica`, `orientacion`, `medidas`, `precio`\
            from `registros`\
            inner join `codigos`\
            on `registros`.`codigo` = `codigos`.`idCodigos`\
            order by `idRegistros` desc\
            limit 1"
            cursor.execute(sql2)
            for row in cursor:
                vector.append(row)
            repuesta = Consulta(vector['idRegistro'],
                                vector['nombre'],
                                vector['apellido'],
                                vector['tematica'],
                                vector['orientacion'],
                                vector['medida'],
                                vector['precio'])
            print(respuesta)
            

    return vector


   

                 

#(3) Se corre el programa en el servidor
if __name__ == '__main__':
    app.run(debug=True)
   