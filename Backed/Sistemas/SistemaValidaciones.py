




class SistemaValidaciones():
    def __init__ (self):
        pass
    
    def msg(self, mensaje, extra=None):
        print(f'[SistemaValidaciones]>> {mensaje}')
        if extra != None and extra != '' and extra != ' ':
            print('\n>> ',extra)

    def ValidarArchivoConfiguaracion(self):
        self.msg('Validando Archivo de Configuracion')