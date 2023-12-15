from flask import Flask
from flask import jsonify
from flask import request
import pymysql
import pymysql.cursors

'''
test = Flask(__name__)

class contacto:
    def __init__(self,nombre,apellido,email,direccion,localidad,provincia,codigopostal,orientacion,medidas):
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.direccion=direccion
        self.localidad=localidad
        self.provincia=provincia
        self.codigopostal=codigopostal
        self.orientacion=orientacion
        self.medidas=medidas
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email} {self.localidad} {self.provincia} {self.codigopostal} {self.orientacion} {self.medidas}"
    def __del__(self):
        print("El registro se ha cargado en la base de datos")



def ingresardatos():
    nombre = input('Ingresa tu nombre: ')
    apellido = input('Ingresa tu apellido: ')
    email = input('Ingresa tu email: ')
    direccion = input('Ingresa tu direccion: ')
    localidad = input('Ingresa tu localidad: ')
    provincia = input('Ingresa tu provincia: ')
    codigopostal = input('Ingresa tu codigo postal: ')
    orientacion = input('Ingresa tu orientacion: ')
    medidas = input('Ingresa tu medida: ')
    registro = contacto(nombre,apellido,email,direccion,localidad,provincia,codigopostal,orientacion,medidas,)
    print (registro)
    connection = pymysql.connect (host='localhost',
                                  user='root',
                                  password='',
                                  database='mydb',
                                  charset='utf8',
                                  cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `mydb.Formulario` (`nombre`,`apellido`,`email`,`direccion`,`localidad`,`provincia`,`codigopostal`,`Codigos_idCodigos`) \
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql,
                           registro['nombre'],
                           registro['apellido'],
                           registro['email'],
                           registro['direccion'],
                           registro['localidad'],
                           registro['provinicia'],
                           registro['codigopostal'],
                           registro['Codigos_idCodigos'])
            connection.commit()
    

ingresardatos()



# Ejecutar continuamente
#if __name__ == '__main__':
#   test.run(debug=True)
'''