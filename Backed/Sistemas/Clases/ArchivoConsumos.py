


class CListaconsumos():
    def __init__(self):
        self.Listaconsumos = []
    
    def desplegar(self):
        print('[Lista consumos]--')
        if self.Listaconsumos != None or self.Listaconsumos != []:
            for consumocliente in self.Listaconsumos:
                consumocliente.desplegar()
        print('[Fin Lista consumos]--')

class CConsumoCliente():
    def __init__(self, nitcliente, idinstancia, tiempo, fechahora):
        self.nitcliente = nitcliente
        self.idinstancia = idinstancia
        self.tiempo = tiempo
        self.fechahora = fechahora
    
    def desplegar(self):
        print(f'   Nit Cliente: {self.nitcliente}, Id Instancia: {self.idinstancia}, Tiempo: {self.tiempo}, Fecha Hora: {self.fechahora}')
        
    