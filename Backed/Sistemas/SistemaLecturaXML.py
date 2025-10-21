from xml.dom.minidom import Document, parse, parseString

from Clases.ArchivoConfiguracion import *


class SistemaLeerArchivosXML():
    def __init__(self):
        self.ruta = None
    
    def msg(self, mensaje, extra):
        print(f'[SistemaLeerArchivosXML]>> {mensaje}\n')
        if extra != None and extra != '' and extra != ' ':
            print('>> ',extra)
    
    def asignarruta(self, ruta):
        self.ruta = ruta
        self.msg('Ruta Asignada', ruta)

    def leerArchivo(self):
        if self.ruta == None:
            self.msg('No hay ruta cargada',None)
        else:
            try:
                self.msg('Leyendo archivo XML', None)
            except Exception as e:
                self.msg('Error: en leerArchivo()',e)