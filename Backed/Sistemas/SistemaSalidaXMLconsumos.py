
import os
from xml.dom.minidom import Document, parse, parseString


from Clases.ArchivoConsumos import *

class SistemaSalidaXMLconsumos():
    def __init__(self):
        self.rutasalida = None
        self.ArchivoCons = None

        self.doc = None
        self.root = None

    def GuardarArchivoConfiguraciones(self):
        print('\n\n')
        
        if self.rutasalida != None:
            self.msg('Guardando Archivo Configuraciones...')
            #Iniciar
            self.creararchivoDOC()
            #Segmentar
            self.segmentar_archivo_XML()

            #Guardar
            self.crear_archivo()

        else:
            self.msg('No se ha asignado ruta salida')
    
    
    
    
    def segmentar_archivo_XML(self):
        try:
            self.msg('Segmenetar XML')
        except Exception as e:
            self.msg('Error en segmentar_archivo_XML()',e)
    
    def creararchivoDOC(self):
        try:
            self.msg('Creando Doc and root')
            self.doc = Document()
            self.root = self.doc.createElement('listadoConsumos')
            self.doc.appendChild(self.root)
        except Exception as e:
            self.msg("!!! Error en creararchivoDOC() al crear el archivo DOC!!!\n",e)
    
    def crear_archivo(self):
        try:
            contenido = self.doc.toprettyxml(indent=" ", encoding="UTF-8")
            with open(self.rutasalida, 'wb') as archivo:
                archivo.write(contenido)
            self.msg(">> Archivo creado o sobrescrito correctamente.\n")
        except Exception as e:
            self.msg(f'!!! Error al crear_archivo !!!\n',e)

    
    def msg(self, mensaje, extra=None):
        print(f'[SistemaSalidaXMLconsumos]>> {mensaje}')
        if extra != None and extra != '' and extra != ' ':
            print('\n>> ',extra)


    def asignarruta(self, ruta):
        self.rutasalida = ruta
        self.msg(f'Ruta asignada: {ruta}')
    
    def asignarArchivoConfiguraciones(self, archivo):
        self.ArchivoCons = archivo
        self.msg(f'Archivo cargado')