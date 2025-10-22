
import os
from xml.dom.minidom import Document, parse, parseString


from Clases.ArchivoConfiguracion import *

class SistemaSalidaXML():
    def __init__(self):
        self.rutasalida = None
    
    def asignarruta(self, ruta):
        self.rutasalida = ruta

    def msg(self, mensaje, extra=None):
        print(f'[SistemaLeerArchivosXML]>> {mensaje}')
        if extra != None and extra != '' and extra != ' ':
            print('\n>> ',extra)

    def GuardarArchivoConfiguraicones(self):
        print('\n\n')
        
        if self.rutasalida != None:
            self.msg('Guardando Archivo Configuraciones...')
            print(self.rutasalida)
        else:
            self.msg('No se ha asignado ruta salida')
        
    def crear_archivo(self, contenido):
        try:
            with open(self.rutasalida, 'wb') as archivo:
                archivo.write(contenido)
            print(">> Archivo creado o sobrescrito correctamente.\n")
        except Exception as e:
            print(f'!!! Error al crear_archivo !!!\n',e)