
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
        print(f">>>ID: {self.id}, Nombre: {self.nombre}, Abreviatura: {self.abreviatura}, Metrica: {self.metrica}, Tipo: {self.tipo}, Valor x Hora: {self.valorxhora}")

#[B1]#######################################################

class CCategoria():
    def __init__(self, id, nombre, descripcion, cargatrabajo):
        self.id = id
        self.nombre = nombre
        self.descipcion = descripcion
        self.cargatrabajo = cargatrabajo
        self.listaconfiguracion = []
    
    def desplegar(self):
        print('>>> [ Categoria ] ***')
        print(f"--- ID: {self.id}, Nombre: {self.nombre}, Descripcion: {self.descipcion}, Carga de Trabajo: {self.cargatrabajo}")
        print('>>>>>[Lista Configuraciones]')
        for configuracion in self.listaconfiguracion:
            configuracion.desplegar()
        print('>>>>> [Fin Lista Configuraciones]')
        print('>>>[Fin Categoria ] ***')


#[B2]#######################################################

class CConfiguracion():
    def __init__(self,id, nombre, descipcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descipcion
        self.listarecursoconfiguracion = []

    def desplegar(self):
        print('   ++ [ CONFIGURACION ]')
        print(f"      ID: {self.id}, Nombre: {self.nombre}, Descripcion: {self.descripcion}")
        print('        ** [Lista Recursos]')
        for recurso in self.listarecursoconfiguracion:
            recurso.desplegar()
        print('        ** [Fin Lista Recursos]')
        print('   ++ [FIN CONFIGURACION ]')

#[B3]#######################################################

class CRecursoConfiguracion():
    def __init__(self, id, cantidadrecurso):
        self.id = id
        self.cantidadrecurso = cantidadrecurso
    
    def desplegar(self):
        print(f"             ID: {self.id}, Cantidad Recurso: {self.cantidadrecurso}")


#[C1]#######################################################

class CCliente():
    def __init__(self, nit, nombre, usuario, clave, direccion,correoelectronico):
        self.nit = nit
        self.nombre = nombre
        self.usuario = usuario
        self.clave = clave
        self.direccion = direccion
        self.correoelectronico = correoelectronico
        self.listainstancias = []
    
    def desplegar(self):
        print('>>> [Cliente] ***')
        print(f"--- NIT: {self.nit}, Nombre: {self.nombre}, Usuario: {self.usuario}, Clave: {self.clave}, Direccion: {self.direccion}, Correo Electronico: {self.correoelectronico}")
        print('---- [Instancias]')
        for instancia in self.listainstancias:
            instancia.desplegar()
        print('---- [Fin Instancias]')
        print('>>> [Fin Cliente] ***')
        
#[C2]#######################################################

class CInstancias():
    def __init__(self, id, idconfiguracion, nombre, fechainicio, estado, fechafinal):
        self.id = id
        self.idconfiguracion = idconfiguracion
        self.nombre = nombre
        self.fechainicio = fechainicio
        self.estado = estado
        self.fechafinal = fechafinal
    
    def desplegar(self):
        print(f"   ID: {self.id}, ID Configuracion: {self.idconfiguracion}, Nombre: {self.nombre}, Fecha Inicio: {self.fechainicio}, Estado: {self.estado}, Fecha Final: {self.fechafinal}")

########################################################
class CArchivoConfiguracion():
    def __init__(self):
        self.listaRecursos = []
        self.listaCategorias = []
        self.listaClientes = []

    def desplegar(self):
        print()
        print('>[ARCHIVO CONFIGURACION]//////////////////////////////////////////////////////////////')
        print('>>[ LISTA RECURSOS ]---')
        for Recurso in self.listaRecursos:
            Recurso.desplegar()
        print('>>[FIN LISTA RECURSOS ]')
        print('\n')
        print('>>[ LISTA CATEGORIAS ]')
        for Categoria in self.listaCategorias:
            Categoria.desplegar()
        print('>>[FIN LISTA CATEGORIAS]')
        print('>>[LISTA CLIENTES]')
        for Cliente in self.listaClientes:
            Cliente.desplegar()
        print('>>[FIN LISTA CLIENTES]')
        print('>[FIN ARCHIVO CONFIGURACION]//////////////////////////////////////////////////////////')
        print()