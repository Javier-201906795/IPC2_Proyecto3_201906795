from xml.dom.minidom import Document, parse, parseString



class SistemaLeerArchivosXMLconsumos():
    def __init__(self):
        self.ruta = None
        self.contenidoXML = None
        self.domXML = None

        self.ArchivoListaConsumos = None
    
    def msg(self, mensaje, extra=None):
        print(f'[SistemaLeerArchivosXMLconsumos]>> {mensaje}')
        if extra != None and extra != '' and extra != ' ':
            print('\n>> ',extra)
    
    def leerArchivo(self):
        if self.ruta == None:
            self.msg('No hay ruta cargada')
        else:
            try:
                self.msg('Leyendo archivo XML')
                print(self.ruta)
                with open(self.ruta, 'r') as archivo:
                    self.contenidoXML = archivo.read()
            except Exception as e:
                self.msg('Error: en leerArchivo()',e)
    
    def asignarruta(self, ruta):
        self.ruta = ruta
        self.msg('Ruta Asignada', ruta)

    def obtenerArchivoConsumo(self):
        return self.ArchivoListaConsumos
    
    def SegmentarArchivo(self):
        try:
            self.msg('Convertir a DOM')
            self.domXML = parseString(self.contenidoXML)
            # print(self.domXML.toxml())
            self.msg('Segmentar Archivo')
            Dom = self.domXML
            if Dom != None:
                #Obtenre ArchivoConfiguracion Solo el primero
                XMLArchivoconsumos = Dom.getElementsByTagName('listadoConsumos')[0]
                #Recorrer listas
                XMLVariosConsumos = XMLArchivoconsumos.getElementsByTagName('consumo')
                #Consumos
                for XMLConsumo in XMLVariosConsumos:
                    # print(XMLConsumo.toxml())
                    XMLConnitcliente = XMLConsumo.getAttribute('nitCliente').strip()
                    XMLConidInstancia = XMLConsumo.getAttribute('idInstancia').strip()
                    
                    XMLContiempo = XMLConsumo.getElementsByTagName('tiempo')[0].firstChild.data.lstrip().lower()

                    XMLConfechahora = XMLConsumo.getElementsByTagName('fechaHora')[0].firstChild.data.lstrip().lower()
                    print(XMLConfechahora)




                
        

        except Exception as e:
            self.msg('Error en SegmentarArchivo()',e)