




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
            self.msg('Validar Lista Recursos')
            for Recurso in self.ListaRecursos:
                #Validar Recurso
                self.ValidacionRecurso(Recurso)
            
            #Recorrer Lista Clientes
            self.msg('Validar Lista Clientes')
            for Cliente in self.ListaClientes:
                #Validar Cliente
                self.ValidacionCliente(Cliente)
            
    def ValidacionCliente(self, cliente):
        try:
            #Datos A validar
            nit = cliente.nit
            print(nit)

        except Exception as e:
            self.mgs('Erro en ValidacioCliente()',e)


    def ValidacionRecurso(self,recurso):
        try:
            recurso.desplegar()
            #Evaluar tipo
            tipo = self.validarOpciones(recurso.tipo,['hardware','software'])
            recurso.tipo = tipo
            print(recurso.tipo)
            
        except Exception as e:
            self.msg('Error en ValidacionRecurso()',e)



    def validarOpciones(self, opcionevaluar, opcionesvalidas):
        try:
            #Convertir variable a minusculuas y quitar espacios
            opcionevaluar = str(opcionevaluar).lstrip().lower()
            #Lista Opciones Validas
            opcionesvalalidas = opcionesvalidas
            #Evaluar
            if opcionevaluar in opcionesvalalidas:
                self.msg(f'recurso tipo: opcion valida -> {opcionevaluar}')
            else:
                self.msg(f'recurso tipo: opcion Invalida -> {opcionevaluar}')
            #Retornoar

            return opcionevaluar
        except Exception as e:
            self.msg('Error en validarOpciones()',e)



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
