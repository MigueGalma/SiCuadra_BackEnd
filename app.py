from flask import Flask
from flask import jsonify
from flask import request
import pymysql
import pymysql.cursors
import objects

app = Flask(__name__)

# (1) Se importa los datos de la pagina del Formulario como un JSON

registro = contacto()

@app.route("/registro", method='POST')
def importingData():
    registro = jsonify(contacto.json)
    registro.headers.add('Access-Control-Allow-Origin', '*')
    data = request.form
    connection = pymysql.connect (host='localhost',
                              user='root',
                              password='miguel1992',
                              database='mydb',
                              charset='utf8',
                              cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `Formulario` (`nombre`,`apellido`,`email`,`direccion`,`localidad`,`provincia`,`codigopostal`) \
            VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql,
                           (data['nombre'],
                            data['apellido'],
                            data['email'],
                            data['direccion'],
                            data['localidad'],
                            data['provinicia'],
                            data['codigopostal']))
            connection.commit()
        print(data['nombre'])
        print(data['apellido'])
        print(data['email'])
        print(data['direccion'])
        print(data['localidad'])
        print(data['provinicia'])
        print(data['codigopostal'])
    return registro

# (2) Se exporta los datos hacia el FrontEnd

@app.route("/respuesta", method='GET')
def enviarPedido():
    data=[]
    connection = pymysql.connect (host='localhost',
                              user='root',
                              password='miguel1992',
                              database='mydb',
                              charset='utf8',
                              cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT `Formulario.nombre`,`Formulario.apellido`,`Codigos.orientacion`,`Codigos.precio`,`Codigos.precios`\
            FROM `Formulario`\
            FULL OUTER JOIN `Codigos`\
            ON `Formulario.Codigo_idCodigos`= `Codigos.idCodigos`\
            WHERE MAX(`Formulario.idFormulario`)"
            for row in cursor:
                data.append(row)

        respuesta = jsonify(data)
        respuesta.headers.add('Access-Control-Allow-Origin', '*')
    return respuesta

#(3) Ejecutar el programa continuamente en el servidor
#if __name__ == '__main__':
#    app.run(debug=True)

    




    




