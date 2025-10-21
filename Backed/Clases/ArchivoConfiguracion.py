
########################################################

class CRecurso():
    def __init__(self,id,nombre,abreviatura,metrica,tipo,valorxhora):
        self.id = id
        self.nombre = nombre
        self.abreviatura = abreviatura
        self.metrica = metrica
        self.tipo = tipo
        self.valorxhora = valorxhora
    
    def desplegar(self):
        print(f"ID: {self.id}, Nombre: {self.nombre}, Abreviatura: {self.abreviatura}, Metrica: {self.metrica}, Tipo: {self.tipo}, Valor x Hora: {self.valorxhora}")



########################################################
class CArchivoConfiguracion():
    def __init__(self):
        pass