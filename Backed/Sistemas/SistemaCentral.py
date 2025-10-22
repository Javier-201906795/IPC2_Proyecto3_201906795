import os

from SistemaLecturaXML import SistemaLeerArchivosXML

class SistemaCentral():
    def __init__(self):
        self.SisLeerArhvXML = SistemaLeerArchivosXML()
        self.ArchivoConfiguracion = None
    
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
        pass






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


####################################################################