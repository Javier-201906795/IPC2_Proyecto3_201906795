from flask import Flask, request, render_template, redirect, url_for
from flask_cors import CORS
from flask.json import jsonify


import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "Sistemas"))
from SistemaCentral import SistemaCentral


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

@app.route('/procesarConfig',   methods=['GET','POST'])
def procesarConfig():
    try:
        SisCntr = app.config['sistema_central']
        #Ruta
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.abspath(os.path.join(ruta_actual, '.', 'entrada.xml'))
        print(ruta_archivo)
        #Leer Archivo
        SisCntr.LeerArchivo(ruta_archivo)
        #Validar Archivo
        SisCntr.ValidarArchivo()
        #Recupear Erroes
        mensajeerror = SisCntr.mensajeErroresXML
        print(mensajeerror)
        return jsonify({"errores": mensajeerror})
    except Exception as e:
        print('!!! Error FLASK inicio() !!!\n',e)

@app.route('/subirConfig', methods=['POST'])
def subirConfig():
    try:
        mensaje = '' 

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
    

# ---- CRUD Recursos ----
@app.route('/resources', methods=['GET','POST'])
def resources():
    SisCntr = app.config['sistema_central']
    try:
        if request.method == 'GET':
            # Debe devolver lista serializable
            return jsonify(SisCntr.list_recursos()), 200
        data = request.json
        SisCntr.add_recurso(data)  # adaptar nombre y firma
        return jsonify({"message":"recurso creado"}), 201
    except Exception as e:
        print("Error resources:", e)
        return jsonify({"error": str(e)}), 500

@app.route('/resources/<string:res_id>', methods=['GET','PUT','DELETE'])
def resource_item(res_id):
    SisCntr = app.config['sistema_central']
    try:
        if request.method == 'GET':
            return jsonify(SisCntr.get_recurso(res_id)), 200
        if request.method == 'PUT':
            data = request.json
            SisCntr.update_recurso(res_id, data)
            return jsonify({"message":"recurso actualizado"}), 200
        if request.method == 'DELETE':
            SisCntr.delete_recurso(res_id)
            return jsonify({"message":"recurso eliminado"}), 200
    except Exception as e:
        print("Error resource_item:", e)
        return jsonify({"error": str(e)}), 500

# ---- CRUD Categorias ----
@app.route('/categories', methods=['GET','POST'])
def categories():
    SisCntr = app.config['sistema_central']
    try:
        if request.method == 'GET':
            return jsonify(SisCntr.list_categorias()), 200
        data = request.json
        SisCntr.add_categoria(data)
        return jsonify({"message":"categoria creada"}), 201
    except Exception as e:
        print("Error categories:", e)
        return jsonify({"error": str(e)}), 500

@app.route('/categories/<string:cat_id>', methods=['GET','PUT','DELETE'])
def category_item(cat_id):
    SisCntr = app.config['sistema_central']
    try:
        if request.method == 'GET':
            return jsonify(SisCntr.get_categoria(cat_id)), 200
        if request.method == 'PUT':
            data = request.json
            SisCntr.update_categoria(cat_id, data)
            return jsonify({"message":"categoria actualizada"}), 200
        if request.method == 'DELETE':
            SisCntr.delete_categoria(cat_id)
            return jsonify({"message":"categoria eliminada"}), 200
    except Exception as e:
        print("Error category_item:", e)
        return jsonify({"error": str(e)}), 500





#Ejecutar
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 4000, debug=True)