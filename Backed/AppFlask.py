from flask import Flask, request, render_template, redirect, url_for
from flask_cors import CORS
from flask.json import jsonify

from Sistemas.SistemaCentral import SistemaCentral
import os

#Crear app
app = Flask(__name__)
#CORS
cors = CORS(app)



app.config['sistema_central']  = SistemaCentral()





@app.route('/',   methods=['GET','POST'])
def inicio():
    try:
        return 'hola'
    except Exception as e:
        print('!!! Error FLASK inicio() !!!\n',e)

@app.route('/subirConfig', methods=['POST'])
def subirConfig():
    try:
        mensaje = ''  # ✅ se inicializa correctamente

        if 'archivo' not in request.files:
            mensaje = '!! No se encontró el archivo !!'
            print(mensaje)
            return mensaje, 400

        archivo = request.files['archivo']

        if archivo.filename == '':
            mensaje = '!! No se seleccionó ningún archivo !!'
            print(mensaje)
            return mensaje, 400

        # Si no hubo errores, procesar el archivo
        print('>>> Leyendo archivo...')
        ruta_archivo = os.path.join(os.getcwd(), 'entrada.xml')
        archivo.save(ruta_archivo)
        print('>>> Se subió el archivo correctamente en:', ruta_archivo)

        return 'Archivo Configuración recibido correctamente', 200

    except Exception as e:
        print('!!! Error FLASK subirConfig() !!!\n', e)
        return f'Error en el servidor Flask: {str(e)}', 500





#Ejecutar
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 4000, debug=True)