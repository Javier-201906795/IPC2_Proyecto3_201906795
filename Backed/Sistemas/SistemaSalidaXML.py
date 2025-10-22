
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
            #Iniciar
            self.creararchivoDOC()
            #Segmentar
            
            #Guardar
            self.crear_archivo()

        else:
            self.msg('No se ha asignado ruta salida')
        
    def creararchivoDOC(self):
        try:
            self.msg('Creando Doc and root')
            self.doc = Document()
            self.root = self.doc.createElement('archivoConfiguraciones')
            self.doc.appendChild(self.root)
        except Exception as e:
            self.msg("!!! Error al crear el archivo DOC!!!\n",e)
    
    def crear_archivo(self):
        try:
            contenido = self.doc.toprettyxml(indent=" ", encoding="UTF-8")
            with open(self.rutasalida, 'wb') as archivo:
                archivo.write(contenido)
            self.msg(">> Archivo creado o sobrescrito correctamente.\n")
        except Exception as e:
            self.msg(f'!!! Error al crear_archivo !!!\n',e)

    def msg(self, mensaje, extra=None):
        print(f'[SistemaLeerArchivosXML]>> {mensaje}')
        if extra != None and extra != '' and extra != ' ':
            print('\n>> ',extra)