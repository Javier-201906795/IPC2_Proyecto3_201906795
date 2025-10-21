from xml.dom.minidom import Document, parse, parseString

from Clases.ArchivoConfiguracion import *


class SistemaLeerArchivosXML():
    def __init__(self):
        self.ruta = None
        self.contenidoXML = None
        self.domXML = None
    
    def msg(self, mensaje, extra=None):
        print(f'[SistemaLeerArchivosXML]>> {mensaje}')
        if extra != None and extra != '' and extra != ' ':
            print('\n>> ',extra)
    
    def asignarruta(self, ruta):
        self.ruta = ruta
        self.msg('Ruta Asignada', ruta)

    def leerArchivo(self):
        if self.ruta == None:
            self.msg('No hay ruta cargada')
        else:
            try:
                self.msg('Leyendo archivo XML')
                with open(self.ruta, 'r') as archivo:
                    self.contenidoXML = archivo.read()
            except Exception as e:
                self.msg('Error: en leerArchivo()',e)
    
    def SegmentarArchivo(self):
        try:
            self.msg('Convertir a DOM')
            self.domXML = parseString(self.contenidoXML)
            # print(self.domXML.toxml())
            self.msg('Segmentar Archivo')
            #Obtener lista recursos
            self.obtenerlistaRecursos()

        

        except Exception as e:
            self.msg('Error en SegmentarArchivo()',e)
    
    def obtenerlistaRecursos(self):
        try:
            self.msg('Obtener Lista Recursos')
        except Exception as e:
            self.msg('Error en obtenerlistaRecursos()',e)