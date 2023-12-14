from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
import pymysql
import pymysql.cursors


conexion = Flask(__name__)

@conexion.route("/registro", methods=['POST','GET'])
def importarJSON():
    data = request.form
    return data
    
if __name__ == '__main__':
    conexion.run(debug=True)
