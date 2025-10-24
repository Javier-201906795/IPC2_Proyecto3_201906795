
from datetime import date, datetime



class SistemaValidaciones():
    def __init__ (self):
        self.msjErrores = ''
        self.ArchivoConfiguracion = None
        self.ListaRecursos = None
        self.ListaCategorias = None
        self.ListaClientes = None

        self.ArchivoConsumos = None
    
    
    def obtenerArchivoConfiguracion(self):
        return self.ArchivoConfiguracion
    
    def obtenermensajeerrores(self):
        return self.msjErrores

    def ValidarArchivoConsumos(self):
        try:
            self.msg('Validando Archivo consumos')
            if self.ArchivoConsumos != None:
                ListaConsumos = self.ArchivoConsumos.Listaconsumos
                for Consumo in ListaConsumos:
                    #Obtener datos
                    Consumo.desplegar()
                    
                    # print(Consumo.idinstancia)
                    # print(Consumo.tiempo)
                    # print(Consumo.fechahora)
                    #Validar nit
                    Consumo.nitcliente =self.validarnit(Consumo.nitcliente)
                    #Validar tiempo
                    Consumo.tiempo = self.validartiempoconsumido(Consumo.tiempo)
                    #Validar fechaHora

                    Consumo.desplegar()
                    print('-------')

        except Exception as e:
            self.msg('ValidarArchivoConsumos',e)
    
    def validartiempoconsumido(self, txttiempo):
        try:
            tiempo = str(txttiempo).lstrip().rstrip()
            fraces = tiempo.split()
            numero = 0
            palabra = ''
            encontronumero = False  
            for palabra in fraces:
                #Tratar convertir en numero
                try:
                    numero = float(palabra)
                    if encontronumero == False:
                        encontronumero = True
                except:
                    #Obtener Tag
                    if palabra != '' or palabra != None and encontronumero == True:
                        tag = str(palabra).strip()

            return f'{numero} {tag}'
        except Exception as e:
            self.msg('Error en validartiempoconsumido()',e)


    def ValidarArchivoConfiguaracion(self):
        try:
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
                print()
        except Exception as e:
            self.msg('Error en ValidarArchivoConfiguaracion()',e)

    def ValidacionCliente(self, cliente):
        try:
            ##################
            #VALIDACION NIT
            nit = cliente.nit
            cliente.nit = self.validarnit(nit)
            print('Nit: ',cliente.nit)
            
            ##################
            #VALIDACION LISTA INSTANCIAS
            listainstancias = cliente.listainstancias
            self.validainstancias(listainstancias)


        except Exception as e:
            self.msg('Erro en ValidacioCliente()',e)

    def validainstancias(self, listainstancias):
        try:
            self.msg('Validar Lista Instancias')
            for lista in listainstancias:
                for instancia in lista:
                    # instancia.desplegar()  
                    estado = instancia.estado
                    fechainicial = instancia.fechainicio
                    fechafinal = instancia.fechafinal
                    #Validar Fecha Inicial
                    print('--------')
                    print('>Fecha Inicial: ', fechainicial) 
                    instancia.fechainicio = self.validarfecha(fechainicial)
                    print('>>Fecha Inicial: ', instancia.fechainicio) 
                    print('--')


                    print('>Estado: ',estado,' Fecha Final: ', fechafinal) 
                    #Validar Estado
                    instancia.estado = self.validarOpciones(estado,['cancelada','Cancelada','Vigente','vigente'])
                    #Validar Fecha Final
                    instancia.fechafinal = self.validarfecha(fechafinal)
                    print('>>Estado: ',instancia.estado,' Fecha Final: ', instancia.fechafinal) 
                    print('--------')
                    print()
            
            print('Erorres Acumulados: ', self.msjErrores)
        except Exception as e:
            self.msg('Error en validainstancias()',e)
    
    def validarfecha(self, txtfecha):
        try:
            temptxtfecha = txtfecha
            txtfecha = str(txtfecha).strip().lower()
            #Segmentar por palabra
            frase = txtfecha.split()
            banderaprimero = False
            for palabra in frase:
                if '/' in palabra and banderaprimero == False:
                    txtfecha = palabra
                    banderaprimero = True
            #Validar si hay fecha
            if banderaprimero == False:
                #No hay fecha
                mensaje=f'fecha Invalida! no se encontro la fecha-> {temptxtfecha}'
                self.msg(mensaje)
                self.msjErrores += mensaje+'\n'
                txtfecha = date.today().strftime("%d/%m/%Y")
            else:
                #Si hay fecha
                try:
                    #pasar a formato
                    txtfecha = datetime.strptime(txtfecha, "%d/%m/%Y")
                    txtfecha = str(txtfecha.strftime("%d/%m/%Y"))
                except:
                    mensaje=f'fecha Invalida! el formato no esta correcto-> {temptxtfecha}'
                    self.msg(mensaje)
                    self.msjErrores += mensaje+'\n'
                    txtfecha = date.today().strftime("%d/%m/%Y")

            return txtfecha
        except Exception as e:
            self.msg('Error en validarfecha()',e)

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
                        # self.msg(f'nit valido -> {nit}')
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
            tempopcionesvalor = opcionevaluar
            #Convertir variable a minusculuas y quitar espacios
            opcionevaluar = str(opcionevaluar).strip().lower()
            #Lista Opciones Validas
            opcionesvalalidas = opcionesvalidas
            #Evaluar
            if opcionevaluar in opcionesvalalidas:
                pass
                # self.msg(f'recurso tipo: opcion valida -> {opcionevaluar}')
            else:
                opcionevaluar = opcionesvalalidas[0]
                mensaje = f'recurso tipo: opcion Invalida! -> {tempopcionesvalor}'
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

    def asignarArchivoConsumoClientes(self,Clase):
        try:
            self.msg('Se asigno el archivo consumos Clientes')
            self.ArchivoConsumos = Clase
        except Exception as e:
            self.msg('Error en asignarArchivoConsumoClientes()',e)