




class SistemaValidaciones():
    def __init__ (self):
        self.msjErrores = ''
        self.ArchivoConfiguracion = None
        self.ListaRecursos = None
        self.ListaCategorias = None
        self.ListaClientes = None
    
    

    def ValidarArchivoConfiguaracion(self):
        self.msg('Validando Archivo de Configuracion')
        if self.ArchivoConfiguracion != None:
            #Recorrer Lista Recursos
            for Recurso in self.ListaRecursos:
                self.ValidacionRecurso(Recurso)
            
    
    def ValidacionRecurso(self,recurso):
        try:
            self.msg('Validando Recurso')
            recurso.desplegar()
            #Evaluar tipo
            opcionevaluar = str(recurso.tipo).lower()
            #Lista Opciones Validas
            opcionesvalalidas = ['hardware','software']
            #Evaluar
            if opcionevaluar in opcionesvalalidas:
                self.msg(f'recurso tipo: opcion valida -> {opcionevaluar}')
            else:
                self.msg(f'recurso tipo: opcion Invalida -> {opcionevaluar}')
        except Exception as e:
            self.msg('Error en ValidacionRecurso()',e)





    def msg(self, mensaje, extra=None):
        print(f'[SistemaValidaciones]>> {mensaje}')
        if extra != None and extra != '' and extra != ' ':
            print('\n>> ',extra)

    def asignarArchivoConfiguracion(self,Clase):
        self.ArchivoConfiguracion = Clase
        self.msg('Se asigno el Archivo de Configuracion')
        try:
            self.ListaRecursos = self.ArchivoConfiguracion.listaRecursos
            self.ListaCategorias = self.ArchivoConfiguracion.listaCategorias
            self.ListaClientes = self.ArchivoConfiguracion.listaClientes
        except Exception as e:
            self.msg('Error en  asignarArchivoConfiguracion()',e)
