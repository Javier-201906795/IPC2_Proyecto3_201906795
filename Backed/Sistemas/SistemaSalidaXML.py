
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
            self.segmentar_archivo_XML()

            #Guardar
            self.crear_archivo()

        else:
            self.msg('No se ha asignado ruta salida')
    
    
    
    
    def segmentar_archivo_XML(self):
        try:
            self.msg('segmentar archivo...')
            root = self.root
            doc = self.doc
            ListaRecursos = self.ArchivoConfig.listaRecursos
            ListaCategorias = self.ArchivoConfig.listaCategorias
            ListaClientes = self.ArchivoConfig.listaClientes

            

            xmlListaRecurso = doc.createElement('listaRecursos')
            root.appendChild(xmlListaRecurso)

            
            #Lista Recursos
            for recurso in ListaRecursos:
                xmlRecurso = doc.createElement('recurso')
                xmlListaRecurso.appendChild(xmlRecurso)

                xmlRecurso.setAttribute("id", f"{recurso.id }")

                xmlRnombre = doc.createElement('nombre')
                xmlRecurso.appendChild(xmlRnombre)
                txt= doc.createTextNode(f'{recurso.nombre}')
                xmlRnombre.appendChild(txt)

                xmlRabreviatura = doc.createElement('abreviatura')
                xmlRecurso.appendChild(xmlRabreviatura)
                txt= doc.createTextNode(f'{recurso.abreviatura}')
                xmlRabreviatura.appendChild(txt)

                xmlMetrica = doc.createElement('metrica')
                xmlRecurso.appendChild(xmlMetrica)
                txt= doc.createTextNode(f'{recurso.metrica}')
                xmlMetrica.appendChild(txt)

                xmltipo = doc.createElement('tipo')
                xmlRecurso.appendChild(xmltipo) 
                txt= doc.createTextNode(f'{recurso.tipo}')
                xmltipo.appendChild(txt)

                xmlValorxhora = doc.createElement('valorXhora')
                xmlRecurso.appendChild(xmlValorxhora)
                txt= doc.createTextNode(f'{recurso.valorxhora}')    
                xmlValorxhora.appendChild(txt)
                
                


            
            

        except Exception as e:
            self.msg(f'!!! Error al segmentar_archivo_XML !!!\n',e)
        
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