from flask import Flask
from flask import jsonify
from flask import request
import pymysql
import pymysql.cursors

app = Flask(__name__)

# (1) Se importa los datos de la pagina del Formulario como un JSON

@app.route("file:///C:/Users/HP/Desktop/Team_12/Sicuadra2/form.html", method='POST')
def importingData():
        