from xml.dom.minidom import Document, parse, parseString

from Clases.ArchivoConfiguracion import *


class SistemaLeerArchivosXML():
    def __init__(self):
        self.ruta = None
        self.contenidoXML = None
        self.domXML = None
        self.XMLArchivoconfiguracion = None

        self.CArchivoConfiguracion = CArchivoConfiguracion()
        self.ListaRecuros = self.CArchivoConfiguracion.listaRecursos
        self.ListaCategorias = self.CArchivoConfiguracion.listaCategorias
        self.ListaClientes = self.CArchivoConfiguracion.listaClientes
        
    
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
            Dom = self.domXML
            if Dom != None:
                #Obtenre ArchivoConfiguracion Solo el primero
                self.XMLArchivoconfiguracion = Dom.getElementsByTagName('archivoConfiguraciones')[0]
                # print(self.XMLArchivoconfiguracion.toxml())
                #Obtener lista recursos
                self.obtenerlistaRecursos()

        

        except Exception as e:
            self.msg('Error en SegmentarArchivo()',e)
    
    def obtenerlistaRecursos(self):
        try:
            self.msg('Obtener Lista Recursos')
            XMLlistaRecursos = self.XMLArchivoconfiguracion.getElementsByTagName('listaRecursos')[0]
            # print(XMLlistaRecursos.toxml())
            #Obtener Recursos
            XMLVariosRecursos = XMLlistaRecursos.getElementsByTagName('recurso')
            for XMLRecurso in XMLVariosRecursos:
                print(XMLRecurso.toxml())
                Recursoid = XMLRecurso.getAttribute('id')
                RecursoNombre = XMLRecurso.getElementsByTagName('nombre')[0].firstChild.data.lstrip()
                RecursoAbreviatura = XMLRecurso.getElementsByTagName('abreviatura')[0].firstChild.data.strip()
                RecursoMetrica = XMLRecurso.getElementsByTagName('metrica')[0].firstChild.data.lstrip()
                RecursoTipo = XMLRecurso.getElementsByTagName('tipo')[0].firstChild.data.lstrip()
                RecursoValorXhora = XMLRecurso.getElementsByTagName('valorXhora')[0].firstChild.data.strip()
                #Convertir a numero
                
                print(Recursoid)
                print(RecursoNombre)
                print(RecursoAbreviatura)
                print(RecursoMetrica)
                print(RecursoTipo)
                print(RecursoValorXhora)
                
                
        except Exception as e:
            self.msg('Error en obtenerlistaRecursos()',e)