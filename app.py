from flask import Flask
from flask import jsonify
from flask import request
import pymysql
import pymysql.cursors
from objects import contacto

app = Flask(__name__)

# (1) Se importa los datos de la pagina del Formulario como un JSON

registro = contacto()

@app.route("/form", method='POST')
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
            sql = "INSERT INTO `mydb.Formulario` (`nombre`,`apellido`,`email`,`direccion`,`localidad`,`provincia`,`codigopostal`) \
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


# (3) Ejecutar el programa continuamente en el servidor
# if __name__ == '__main__':
#   app.run(debug=True)

    




    




