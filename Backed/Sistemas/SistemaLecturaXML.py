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

    def obtenerArchivoConfiguracion(self):
        return self.CArchivoConfiguracion

    
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
                self.obtenerlistaclientes()
                #Imprimir Resultado
                self.CArchivoConfiguracion.desplegar()
        

        except Exception as e:
            self.msg('Error en SegmentarArchivo()',e)
    
    def obtenerlistaclientes(self):
        try:
            self.msg('Obtener lista clientes')
            XMLListaClientes = self.XMLArchivoconfiguracion.getElementsByTagName('listaClientes')[0]
            XMLVariosClientes = XMLListaClientes.getElementsByTagName('cliente')
            for XMLCliente in XMLVariosClientes:
                Cliid= XMLCliente.getAttribute('nit').strip()
                Clinombre= XMLCliente.getElementsByTagName('nombre')[0].firstChild.data.lstrip().lower().rstrip()
                Cliusuario= XMLCliente.getElementsByTagName('usuario')[0].firstChild.data.lstrip().lower().rstrip()
                Cliclave= XMLCliente.getElementsByTagName('clave')[0].firstChild.data.lstrip().lower().rstrip()
                Clidireccion= XMLCliente.getElementsByTagName('direccion')[0].firstChild.data.lstrip().lower()
                # Clidireccion= XMLCliente.getElementsByTagName('direccion')[0].firstChild.data.lstrip().lower()
                ClicorreoElectronico = XMLCliente.getElementsByTagName('correoElectronico')[0].firstChild.data.lstrip().lower().rstrip()
                #Clase
                claseCliente = CCliente(Cliid,Clinombre,Cliusuario,Cliclave,Clidireccion,ClicorreoElectronico)
                
                #Lista Instancias
                ListainstanciasTOTAL = claseCliente.listainstancias
                
                XMLListainstancias = XMLCliente.getElementsByTagName('listaInstancias')
                for XMLLista2Instancias in XMLListainstancias:
                    Listainstancias = []
                    XMLVariasInstancias = XMLLista2Instancias.getElementsByTagName('instancia')
                    for XMLInstancia in XMLVariasInstancias:
                        Insid= XMLInstancia.getAttribute('id').strip()
                        Insidconfiguracion = XMLInstancia.getElementsByTagName('idConfiguracion')[0].firstChild.data.lstrip().lower()
                        Insnombre= XMLInstancia.getElementsByTagName('nombre')[0].firstChild.data.lstrip().lower().rstrip()
                        InsfechaInicio= XMLInstancia.getElementsByTagName('fechaInicio')[0].firstChild.data.lstrip().lower()
                        Insestado = XMLInstancia.getElementsByTagName('estado')[0].firstChild.data.lstrip().lower()
                        InsfechaFinal= XMLInstancia.getElementsByTagName('fechaFinal')[0].firstChild.data.lstrip().lower()
                        #clase
                        claseInstancia = CInstancias(Insid,Insidconfiguracion,Insnombre,InsfechaInicio,Insestado,InsfechaFinal)
                        # claseInstancia.desplegar()
                        #almacenar en lista
                        Listainstancias.append(claseInstancia)
                    
                    # claseCliente.desplegar()
                    #GUARDAR en lista Total
                    ListainstanciasTOTAL.append(Listainstancias)
                #Guardar
                self.ListaClientes.append(claseCliente)
                print('\n')

                    
                




        except Exception as e:
            self.msg('Error en obtenerlistaclientes()',e)
    
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
                Catnombre= XMLCategoria.getElementsByTagName('nombre')[0].firstChild.data.lstrip().lower().rstrip()
                Catdescrpcion= XMLCategoria.getElementsByTagName('descripcion')[0].firstChild.data.lstrip().lower()
                Catcargatrabajo = XMLCategoria.getElementsByTagName('cargaTrabajo')[0].firstChild.data.lstrip().lower().rstrip()
                #Clase
                claseCategoria = CCategoria(Catid,Catnombre, Catdescrpcion,Catcargatrabajo)
                
                #Lista Configuraciones
                ListaConfiguracion =claseCategoria.listaconfiguracion
                XMLListaConfiguraciones = XMLCategoria.getElementsByTagName('listaConfiguraciones')[0]
                XMLVariasConfiguraciones = XMLListaConfiguraciones.getElementsByTagName('configuracion')
                for XMLConfiguracion in XMLVariasConfiguraciones:
                    # print(XMLConfiguracion.toxml())
                    Confid = XMLConfiguracion.getAttribute('id').strip()
                    Confnombre = XMLConfiguracion.getElementsByTagName('nombre')[0].firstChild.data.lstrip().rstrip()
                    Confdescripcion = XMLConfiguracion.getElementsByTagName('descripcion')[0].firstChild.data.lstrip().lower().rstrip()
                    claseConfiguracion = CConfiguracion(Confid,Confnombre,Confdescripcion)
                    claseConfiguracion.desplegar()
                    
                    #Lista Recuros
                    LisaRecuros = claseConfiguracion.listarecursoconfiguracion
                    XMLListaRecursos = XMLListaConfiguraciones.getElementsByTagName('recursosConfiguracion')[0]
                    XMLVariosRecursos = XMLListaRecursos.getElementsByTagName('recurso')
                    for XMLRecurso in XMLVariosRecursos:
                        # print(XMLRecurso.toxml())
                        Recursoid = XMLRecurso.getAttribute('id').strip()
                        Recursocantidad = XMLRecurso.firstChild.data.strip()
                        claseRecurso = CRecursoConfiguracion(Recursoid, Recursocantidad)
                        # claseRecurso.desplegar()
                        #Almacenar
                        LisaRecuros.append(claseRecurso)

                    #Almacenar
                    ListaConfiguracion.append(claseConfiguracion)
                    

                #Imprimir Categorias
                # claseCategoria.desplegar()  
                #Guardar en Lista
                self.ListaCategorias.append(claseCategoria)
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
                RecursoMetrica = XMLRecurso.getElementsByTagName('metrica')[0].firstChild.data.lstrip().rstrip()
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
                    self.msg(f'Error en convertir a numero. {RecursoValorXhora}',e)
                    RecursoValorXhora = 0
                #Crear Clase
                claseRecurso = CRecurso(Recursoid,RecursoNombre,RecursoAbreviatura,RecursoMetrica,RecursoTipo,RecursoValorXhora)
                #Imprimir
                # claseRecurso.desplegar()
                #Guardar
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