
import os
from xml.dom.minidom import Document, parse, parseString


from Clases.ArchivoConfiguracion import *

class SistemaSalidaXML():
    def __init__(self):
        self.rutasalida = None
        self.ArchivoConfig = None

        self.doc = None
        self.root = None
    
    def asignarruta(self, ruta):
        self.rutasalida = ruta
    
    def asignarArchivoConfiguraciones(self, archivo):
        self.ArchivoConfig = archivo

    

    def GuardarArchivoConfiguraicones(self):
        print('\n\n')
        
        if self.rutasalida != None:
            self.msg('Guardando Archivo Configuraciones...')
            print(self.rutasalida)
            print(self.ArchivoConfig)
        else:
            self.msg('No se ha asignado ruta salida')
        
    def creararchivoDOC(self):
        try:
            print('Creando Doc and root')
            self.doc = Document()
            self.root = self.doc.createElement('datoSalida')
            self.doc.appendChild(self.root)
        except Exception as e:
            self.msg("!!! Error al crear el archivo DOC!!!\n",e)

    def msg(self, mensaje, extra=None):
        print(f'[SistemaLeerArchivosXML]>> {mensaje}')
        if extra != None and extra != '' and extra != ' ':
            print('\n>> ',extra)