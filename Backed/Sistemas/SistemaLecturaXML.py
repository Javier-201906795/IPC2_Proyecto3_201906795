from xml.dom.minidom import Document, parse, parseString

from Clases.ArchivoConfiguracion import *


class SistemaLeerArchivosXML():
    def __init__(self):
        self.ruta = None
        self.contenidoXML = None
        self.domXML = None
        self.XMLArchivoconfiguracion = None

        self.CArchivoConfiguracion = CArchivoConfiguracion()
        self.ListaRecursos = self.CArchivoConfiguracion.listaRecursos
        self.ListaCategorias = self.CArchivoConfiguracion.listaCategorias
        self.ListaClientes = self.CArchivoConfiguracion.listaClientes
        
    
    def msg(self, mensaje, extra=None):
        print(f'[SistemaLeerArchivosXML]>> {mensaje}')
        if extra != None and extra != '' and extra != ' ':
            print('\n>> ',extra)
    
    def asignarruta(self, ruta):
        self.ruta = ruta
        self.msg('Ruta Asignada', ruta)

    
    
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
                #Obtener lista Categoria
                self.obtenerlistaCategorias()
                #Obtener lista Clientes

        

        except Exception as e:
            self.msg('Error en SegmentarArchivo()',e)
    
    def obtenerlistaCategorias(self):
        try:
            print('\n')
            self.msg('Obtener Lista Categorias')
            XMLListaCategorias = self.XMLArchivoconfiguracion.getElementsByTagName('listaCategorias')[0]
            #Obtener cagorias
            XMLVariasCategorias = XMLListaCategorias.getElementsByTagName('categoria')
            for XMLCategoria in XMLVariasCategorias:
                # print(XMLCategoria.toxml())
                Catid= XMLCategoria.getAttribute('id').strip()
                Catnombre= XMLCategoria.getElementsByTagName('nombre')[0].firstChild.data.lstrip().lower()
                Catdescrpcion= XMLCategoria.getElementsByTagName('descripcion')[0].firstChild.data.lstrip().lower()
                Catcargatrabajo = XMLCategoria.getElementsByTagName('cargaTrabajo')[0].firstChild.data.lstrip().lower()
                #Clase
                claseCategoria = CCategoria(Catid,Catnombre, Catdescrpcion,Catcargatrabajo)
                
                #Lista Configuraciones
                ListaConfiguracion =claseCategoria.listaconfiguracion
                XMLListaConfiguraciones = XMLListaCategorias.getElementsByTagName('listaConfiguraciones')[0]
                XMLVariasConfiguraciones = XMLListaConfiguraciones.getElementsByTagName('configuracion')
                for XMLConfiguracion in XMLVariasConfiguraciones:
                    # print(XMLConfiguracion.toxml())
                    Confid = XMLConfiguracion.getAttribute('id').strip()
                    Confnombre = XMLConfiguracion.getElementsByTagName('nombre')[0].firstChild.data.lstrip().lower()
                    Confdescripcion = XMLConfiguracion.getElementsByTagName('descripcion')[0].firstChild.data.lstrip().lower()
                    claseConfiguracion = CConfiguracion(Confid,Confnombre,Confdescripcion)
                    # claseConfiguracion.desplegar()
                    
                    #Lista Recuros
                    LisaRecuros = claseConfiguracion.listarecursoconfiguracion
                    XMLListaRecursos = XMLListaConfiguraciones.getElementsByTagName('recursosConfiguracion')[0]
                    XMLVariosRecursos = XMLListaRecursos.getElementsByTagName('recurso')
                    for XMLRecurso in XMLVariosRecursos:
                        # print(XMLRecurso.toxml())
                        Recursoid = XMLRecurso.getAttribute('id').strip()
                        Recursocantidad = XMLRecurso.firstChild.data
                        claseRecurso = CRecursoConfiguracion(Recursoid, Recursocantidad)
                        # claseRecurso.desplegar()
                        #Almacenar
                        LisaRecuros.append(claseRecurso)



                    #Almacenar
                    ListaConfiguracion.append(claseConfiguracion)
                    

                #Imprimir Categorias
                claseCategoria.desplegar()  
                print('\n')  

        except Exception as e:
            self.msg('Error en obtenerlistaCategorias()',e)
    
    def obtenerlistaRecursos(self):
        try:
            print('\n')
            self.msg('Obtener Lista Recursos')
            XMLlistaRecursos = self.XMLArchivoconfiguracion.getElementsByTagName('listaRecursos')[0]
            # print(XMLlistaRecursos.toxml())
            #Obtener Recursos
            XMLVariosRecursos = XMLlistaRecursos.getElementsByTagName('recurso')
            for XMLRecurso in XMLVariosRecursos:
                # print(XMLRecurso.toxml())
                Recursoid = XMLRecurso.getAttribute('id').strip()
                RecursoNombre = XMLRecurso.getElementsByTagName('nombre')[0].firstChild.data.lstrip().lower()
                RecursoAbreviatura = XMLRecurso.getElementsByTagName('abreviatura')[0].firstChild.data.strip().lower()
                RecursoMetrica = XMLRecurso.getElementsByTagName('metrica')[0].firstChild.data.lstrip()
                RecursoValorXhora = XMLRecurso.getElementsByTagName('valorXhora')[0].firstChild.data.strip()
                RecursoTipo = XMLRecurso.getElementsByTagName('tipo')[0].firstChild.data.strip()
                #Quitar espacios en blanco
                try:
                    RecursoTipo = RecursoTipo.split()[0].lower()
                except Exception as e:
                    RecursoTipo = None
                    self.msg(f'Error en ver que tipo es {RecursoTipo}',e)
                
                #Convertir a numero
                try:
                    RecursoValorXhora = float(RecursoValorXhora)
                except Exception as e:
                    RecursoValorXhora = 0
                    self.msg(f'Error en convertir a numero. {RecursoValorXhora}',e)
                #Crear Clase
                claseRecurso = CRecurso(Recursoid,RecursoNombre,RecursoAbreviatura,RecursoMetrica,RecursoTipo,RecursoValorXhora)
                #Imprimir
                claseRecurso.desplegar()
                #Almacenar
                self.ListaRecursos.append(claseRecurso)
                
                
                
        except Exception as e:
            self.msg('Error en obtenerlistaRecursos()',e)

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