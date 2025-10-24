import os

from SistemaLecturaXML import SistemaLeerArchivosXML
from SistemaValidaciones import SistemaValidaciones
from SistemaSalidaXML import SistemaSalidaXML
from SistemaLecturaXMLconsumos import SistemaLeerArchivosXMLconsumos
from SistemaSalidaXMLconsumos import SistemaSalidaXMLconsumos

class SistemaCentral():
    def __init__(self):
        self.SisLeerArhvXML = SistemaLeerArchivosXML()
        self.ArchivoConfiguracion = None
        self.SisSalidaXML = SistemaSalidaXML()

        self.SisVal = SistemaValidaciones()
        self.mensajeErroresXML = None

        self.SisLeerArhvXMLCons = SistemaLeerArchivosXMLconsumos()
        self.ArchivoConsumos = None
        self.SisSalidaXMLCons = SistemaSalidaXMLconsumos()
    
    def LeerArchivo(self,ruta):
        self.SisLeerArhvXML.asignarruta(ruta)
        #Leer Archivo XML
        self.SisLeerArhvXML.leerArchivo()    
        # print(self.SisLeerArhvXML.contenidoXML)
        #Segmentar Archivo XML a clases
        self.SisLeerArhvXML.SegmentarArchivo()
        #Guardar
        self.ArchivoConfiguracion = self.SisLeerArhvXML.obtenerArchivoConfiguracion()
    
    def ValidarArchivo(self):
        #Enviar Archivo
        self.SisVal.asignarArchivoConfiguracion(self.ArchivoConfiguracion)
        #Validar
        self.SisVal.ValidarArchivoConfiguaracion()
        #Guardar
        self.ArchivoConfiguracion = self.SisVal.obtenerArchivoConfiguracion()
        #Mensaje errores
        self.mensajeErroresXML = self.SisVal.obtenermensajeerrores()
        print('msg Errores: ', self.mensajeErroresXML)

    def GuaradarArchivoConfiguraciones(self, ruta):
        #Asignar Ruta
        self.SisSalidaXML.asignarruta(ruta)
        #Enviar informacion
        self.SisSalidaXML.asignarArchivoConfiguraciones(self.ArchivoConfiguracion)
        #Procesar info
        self.SisSalidaXML.GuardarArchivoConfiguraicones()
    
    def LeerBaseDatosArchivoConfiguraciones(self, ruta):
        #Leer Archivo Base Datos Config
        print('Leer DB Config')
        self.LeerArchivo(ruta)
    
    

    ################

    def LeerArchivoConsumos(self,ruta):
        self.SisLeerArhvXMLCons.asignarruta(ruta)
        #Leer Archivo XML
        self.SisLeerArhvXMLCons.leerArchivo()    
        # print(self.SisLeerArhvXML.contenidoXML)
        #Segmentar Archivo XML a clases
        self.SisLeerArhvXMLCons.SegmentarArchivo()
        #Guardar
        self.ArchivoConsumos = self.SisLeerArhvXMLCons.obtenerArchivoListaConsumos()
    
    def ValidarArchivoConsumosCliente(self):
        #Enviar Archivo
        self.SisVal.asignarArchivoConsumoClientes(self.ArchivoConsumos)
        #Validar
        self.SisVal.ValidarArchivoConsumos()
        # #Guardar
        self.ArchivoConsumos = self.SisVal.obtenerArchivoConsumos()
        #Mensaje errores
        self.mensajeErroresXML = self.SisVal.obtenermensajeerrores()
        print('msg Errores: ', self.mensajeErroresXML)
        self.ArchivoConsumos.desplegar()
    
    def GuaradarArchivoConsumos(self, ruta):
        pass
        #Asignar Ruta
        self.SisSalidaXMLCons.asignarruta(ruta)
        # #Enviar informacion
        self.SisSalidaXMLCons.asignarArchivoConfiguraciones(self.ArchivoConfiguracion)
        # #Procesar info
        self.SisSalidaXMLCons.GuardarArchivoConfiguraciones()



####################################################################
print('------[Sistema Central] -------')

#Iniciar Sistema
SisCntr = SistemaCentral()

#Cargar Ruta
# ruta_actual = os.getcwd()
ruta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.abspath(os.path.join(ruta_actual, '..', 'entrada1.xml'))
#Leer Archivo
SisCntr.LeerArchivo(ruta_archivo)
#Validar Archivo
SisCntr.ValidarArchivo()

#Guardar Archivo Configuraciones XML
ruta_archivo_config = os.path.abspath(os.path.join(ruta_actual, '..', 'ArchivoConfiguraciones.xml'))
SisCntr.GuaradarArchivoConfiguraciones(ruta_archivo_config)


#Leer DB Archivo Configuraciones
ruta_DBConfig = os.path.abspath(os.path.join(ruta_actual, '..', 'ArchivoConfiguraciones.xml'))
SisCntr.LeerBaseDatosArchivoConfiguraciones(ruta_DBConfig)


###############

#Leer Archivo Consumos
ruta_archivo = os.path.abspath(os.path.join(ruta_actual, '..', 'entradaconsumos.xml'))
SisCntr.LeerArchivoConsumos(ruta_archivo)

#Validar Archivo
SisCntr.ValidarArchivoConsumosCliente()

#Guardar Archivo Configuraciones XML
ruta_archivo_config = os.path.abspath(os.path.join(ruta_actual, '..', 'ArchivoConsumos.xml'))
SisCntr.GuaradarArchivoConsumos(ruta_archivo_config)


####################################################################

