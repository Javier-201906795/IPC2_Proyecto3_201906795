




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
            ###################################################
            #Recorrer Lista Recursos
            self.msg('Validar Lista Recursos')
            for Recurso in self.ListaRecursos:
                #Validar Recurso
                self.ValidacionRecurso(Recurso)
            #Imprimir Errores
            if self.msjErrores != '':
                print('Errores Recurso: ',self.msjErrores)
            ###################################################
            #Recorrer Lista Clientes
            self.msg('Validar Lista Clientes')
            for Cliente in self.ListaClientes:
                #Validar Cliente
                self.ValidacionCliente(Cliente)
            #Imprimir Errores
            if self.msjErrores != '':
                print('Errores Recurso y Clientes: ',self.msjErrores)
            ###################################################
    def ValidacionCliente(self, cliente):
        try:
            ##################
            #VALIDACION NIT
            nit = cliente.nit
            cliente.nit = self.validarnit(nit)
            print('Nit: ',cliente.nit)
            
            ##################
            #VALIDACION LISTA INSTANCIAS

        except Exception as e:
            self.mgs('Erro en ValidacioCliente()',e)

    def validarnit(self, nit):
        try:
            nit = str(nit).strip()
            #Validar primero digitos
            primerosdatos = nit[:-2]
            banderabien = True
            opcionesvalidasprimero = ['0','1','2','3','4','5','6','7','8','9']
            for caracter in primerosdatos:
                if caracter in opcionesvalidasprimero:
                    pass
                else:
                    banderabien = False
            
            if banderabien == True:
                #Valida ultimos ditigitos
                ##obtener ultimo digito y guio
                ultimodato = nit[-2:]
                ##Validar guion
                guion = ultimodato[:1]
                if guion == '-':
                    #Validar digito validacion
                    digitovalidacion = ultimodato[1:2]
                    opcionesvalidas = ['0','1','2','3','4','5','6','7','8','9','K','k']
                    if digitovalidacion in opcionesvalidas:
                        self.msg(f'nit valido -> {nit}')
                        return nit
                    else:
                        mensaje=f'nit Invalido! ultimo digitio invalido -> {nit}'
                        self.msg(mensaje)
                        self.msjErrores += mensaje+'\n'
                        return "#E1#"+nit
                else:
                    mensaje = f'nit Invalido! Falta Guion en su lugar -> {nit}'
                    self.msg(mensaje)
                    self.msjErrores += mensaje+'\n'
                    return "#E2#"+nit
            else:
                mensaje = f'nit Invalido! primero digitos invalidos -> {nit}'
                self.msg(mensaje)
                self.msjErrores += mensaje+'\n'
                return "#E0#"+nit

        except Exception as e:
            mensaje = f'Error nit Invalido!  -> {nit}'
            self.msg(mensaje)
            self.msjErrores += mensaje+'\n'


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
                opcionevaluar = opcionesvalalidas[0]
                mensaje = f'recurso tipo: opcion Invalida -> {opcionevaluar}'
                self.msg(mensaje)
                self.msjErrores += mensaje+'\n'
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
