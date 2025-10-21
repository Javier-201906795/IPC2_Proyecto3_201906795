
#[A] #####################################################

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

#[B1]#######################################################

class CCategoria():
    def __init__(self, id, nombre, descripcion, cargatrabajo, listaconfiguracion):
        self.id = id
        self.nombre = nombre
        self.descipcion = descripcion
        self.cargatrabajo = cargatrabajo
        self.listaconfiguracion = []
    
    def desplegar(self):
        print(f"ID: {self.id}, Nombre: {self.nombre}, Descripcion: {self.descipcion}, Carga de Trabajo: {self.cargatrabajo}")
        for configuracion in self.listaconfiguracion:
            configuracion.desplegar()


#[B2]#######################################################

class CConfiguracion():
    def __init__(self,id, nombre, descipcion, listarecursoconfiguracion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descipcion
        self.listarecursoconfiguracion = listarecursoconfiguracion

    def desplegar(self):
        print(f"ID: {self.id}, Nombre: {self.nombre}, Descripcion: {self.descripcion}")
        for recurso in self.listarecursoconfiguracion:
            recurso.desplegar()

#[B3]#######################################################

class CRecursoConfiguracion():
    def __init__(self, id, cantidadrecurso):
        self.id = id
        self.cantidadrecurso = cantidadrecurso
    
    def desplegar(self):
        print(f"ID: {self.id}, Cantidad Recurso: {self.cantidadrecurso}")



########################################################
class CArchivoConfiguracion():
    def __init__(self):
        pass