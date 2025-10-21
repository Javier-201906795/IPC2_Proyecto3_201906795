

from SistemaLecturaXML import SistemaLeerArchivosXML


print('------[Sistema Central] -------')
#Iniciar Sistema
SisLeerArhvXML = SistemaLeerArchivosXML()
#Cargar Ruta
SisLeerArhvXML.asignarruta('/')
#Leer Archivo XML
SisLeerArhvXML.leerArchivo()    