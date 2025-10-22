import os

from SistemaLecturaXML import SistemaLeerArchivosXML
from SistemaValidaciones import SistemaValidaciones

class SistemaCentral():
    def __init__(self):
        self.SisLeerArhvXML = SistemaLeerArchivosXML()
        self.ArchivoConfiguracion = None

        self.SisVal = SistemaValidaciones()
    
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
        self.SisVal.ValidarArchivoConfiguaracion()






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


####################################################################

