from flask import Flask, request, render_template, redirect, url_for
from flask_cors import CORS
from flask.json import jsonify


#Crear app
app = Flask(__name__)
#CORS
cors = CORS(app)

@app.route('/',   methods=['GET','POST'])
def inicio():
    try:
        return 'hola'
    except Exception as e:
        print('!!! Error FLASK inicio() !!!\n',e)

@app.route('/subirConfig',   methods=['POST'])
def subirConfig():
    try:
        if request.method == 'POST':
            if 'archivo' not in request.files:
                mensaje = '!! No se encontro el archivo !! '
                print(mensaje)
            return 'hola'
    except Exception as e:
        print('!!! Error FLASK inicio() !!!\n',e)




#Ejecutar
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 4000, debug=True)