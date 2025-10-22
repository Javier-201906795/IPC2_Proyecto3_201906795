import os

from SistemaLecturaXML import SistemaLeerArchivosXML
from SistemaValidaciones import SistemaValidaciones
from SistemaSalidaXML import SistemaSalidaXML

class SistemaCentral():
    def __init__(self):
        self.SisLeerArhvXML = SistemaLeerArchivosXML()
        self.ArchivoConfiguracion = None
        self.SisSalidaXML = SistemaSalidaXML()

        self.SisVal = SistemaValidaciones()
        self.mensajeErroresXML = None
    
    def LeerArchivo(self,ruta):
        self.SisLeerArhvXML.asignarruta(ruta_archivo)
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
        #Procesar info
        self.SisSalidaXML.GuardarArchivoConfiguraicones()




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


####################################################################

