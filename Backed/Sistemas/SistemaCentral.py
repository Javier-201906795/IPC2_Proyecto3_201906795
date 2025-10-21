import os

from SistemaLecturaXML import SistemaLeerArchivosXML




print('------[Sistema Central] -------')
#Iniciar Sistema
SisLeerArhvXML = SistemaLeerArchivosXML()
#Cargar Ruta
ruta_actual = os.getcwd()
ruta_archivo = os.path.abspath(os.path.join(ruta_actual, '..', 'entrada.xml'))
SisLeerArhvXML.asignarruta(ruta_archivo)
#Leer Archivo XML
SisLeerArhvXML.leerArchivo()    
print(SisLeerArhvXML.contenidoXML)