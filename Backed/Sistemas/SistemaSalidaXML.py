
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
            self.ArchivoConfig.desplegar()
            root = self.root
            doc = self.doc
            ListaRecursos = self.ArchivoConfig.listaRecursos
            ListaCategorias = self.ArchivoConfig.listaCategorias
            ListaClientes = self.ArchivoConfig.listaClientes

            

           

            
            #Lista Recursos
            xmlListaRecurso = doc.createElement('listaRecursos')
            root.appendChild(xmlListaRecurso)
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
            
            
            #Lista Categorias
            xmlListaCategorias = doc.createElement('listaCategorias')
            root.appendChild(xmlListaCategorias)

            for categoria in ListaCategorias:
                xmlCategoria = doc.createElement('categoria')
                xmlListaRecurso.appendChild(xmlCategoria)
                
                
                xmlCategoria.setAttribute("id", f"{categoria.id}")

                xmlCatnombre = doc.createElement('nombre')
                xmlCategoria.appendChild(xmlCatnombre)
                txt= doc.createTextNode(f'{categoria.nombre}')
                xmlCatnombre.appendChild(txt)

                xmlCatdescripcion = doc.createElement('descripcion')
                xmlCategoria.appendChild(xmlCatdescripcion)
                txt= doc.createTextNode(f'{categoria.descipcion}')
                xmlCatdescripcion.appendChild(txt)

                xmlCatcargatrabajo = doc.createElement('cargaTrabajo')
                xmlCategoria.appendChild(xmlCatcargatrabajo)
                txt= doc.createTextNode(f'{categoria.cargatrabajo}')
                xmlCatcargatrabajo.appendChild(txt)
                
                #ListaConfiguraciones
                xmlListaConfiguraciones = doc.createElement('listaConfiguraciones')
                xmlCategoria.appendChild(xmlListaConfiguraciones)
                ListaConfiguraciones = categoria.listaconfiguracion

                for config in ListaConfiguraciones:
                    xmlconfiguracion = doc.createElement('configuracion')
                    xmlListaConfiguraciones.appendChild(xmlconfiguracion)

                    xmlconfiguracion.setAttribute("id", f"{config.id}")
                
                    xmlConfnombre = doc.createElement('nombre')
                    xmlconfiguracion.appendChild(xmlConfnombre)
                    txt= doc.createTextNode(f'{config.nombre}')
                    xmlConfnombre.appendChild(txt)

                    xmlConfdescripcion = doc.createElement('descripcion')
                    xmlconfiguracion.appendChild(xmlConfdescripcion)
                    txt= doc.createTextNode(f'{config.descripcion}')
                    xmlConfdescripcion.appendChild(txt)

                    #Lista Recursos
                    xmlListaRecursoConfiguracion = doc.createElement('recursosConfiguracion')
                    xmlconfiguracion.appendChild(xmlListaRecursoConfiguracion)
                    ListaRecursosConfiguracion = config.listarecursoconfiguracion

                    for recursoconfig in ListaRecursosConfiguracion:
                        xmlrecursoconfig = doc.createElement('recurso')
                        xmlListaRecursoConfiguracion.appendChild(xmlrecursoconfig)
                        xmlrecursoconfig.setAttribute("id", f"{recursoconfig.id}")

                        txt= doc.createTextNode(f'{recursoconfig.cantidadrecurso}')
                        xmlrecursoconfig.appendChild(txt)

                #Lista Clientes
                xmlListaClientes = doc.createElement('listaClientes')
                root.appendChild(xmlListaClientes)

                for Cliente in ListaClientes:
                    xmlCliente = doc.createElement('cliente')
                    xmlListaClientes.appendChild(xmlCliente)
                    xmlCliente.setAttribute("id", f"{Cliente.nit}")

                    xmlClinombre = doc.createElement('nombre')
                    xmlCliente.appendChild(xmlClinombre)
                    txt = doc.createTextNode(f'{Cliente.nombre}')
                    xmlClinombre.appendChild(txt)


                    # self.nit = nit
                    # self.nombre = nombre
                    # self.usuario = usuario
                    # self.clave = clave
                    # self.direccion = direccion
                    # self.correoelectronico = correoelectronico
                    # self.listainstancias = []
            
            

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