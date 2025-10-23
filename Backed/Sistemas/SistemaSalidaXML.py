
import os
from xml.dom.minidom import Document, parse, parseString


from Clases.ArchivoConfiguracion import *

class SistemaSalidaXML():
    def __init__(self):
        self.rutasalida = None
        self.ArchivoConfig = None

        self.doc = None
        self.root = None
    
    def asignarruta(self, ruta):
        self.rutasalida = ruta
    
    def asignarArchivoConfiguraciones(self, archivo):
        self.ArchivoConfig = archivo

    

    def GuardarArchivoConfiguraicones(self):
        print('\n\n')
        
        if self.rutasalida != None:
            self.msg('Guardando Archivo Configuraciones...')
            #Iniciar
            self.creararchivoDOC()
            #Segmentar
            self.segmentar_archivo_XML()

            #Guardar
            self.crear_archivo()

        else:
            self.msg('No se ha asignado ruta salida')
    
    
    
    
    def segmentar_archivo_XML(self):
        try:
            self.msg('segmentar archivo...')
            root = self.root
            doc = self.doc
            ListaRecursos = self.ArchivoConfig.listaRecursos
            ListaCategorias = self.ArchivoConfig.listaCategorias
            ListaClientes = self.ArchivoConfig.listaClientes

            

            xmlListaRecurso = doc.createElement('listaRecursos')
            root.appendChild(xmlListaRecurso)

            
            #Lista Recursos
            for recurso in ListaRecursos:
                pass
                #padre
                # XMLrecurso =

            # #Lista invernaderos
            # for i in range(0,self.colainvernaderos.tamano()):
            #     Inv = self.colainvernaderos.Obtener(i+1)
            #     #Datos invernadero
            #     invernadero = doc.createElement('invernadero')
            #     invernadero.setAttribute("nombre", f"{Inv.nombre}")
            #     self.listaInvernaderos.appendChild(invernadero)
            #     Inv.desplegar()
            #     print()
            #     print('> creando invernadero: ',Inv.nombre)

            #     #Lista Planes
            #     listaplanes = doc.createElement('listaPlanes')
            #     invernadero.appendChild(listaplanes)

            #     for h in range(0,Inv.ListaPlanes.tamano()):
            #         #Obtener informacion del historico movimientos
            #         Movmientos = Inv.historialmovimientos.Obtener(h+1)
            #         #Obtener informacion de Lista plantes
            #         Planinfo = Inv.ListaPlanes.Obtener(h+1)
            #         #Obtener tiempo optimo
            #         TiempooptimoInv = Inv.historiatiempooptimo.Obtener(h+1)
            #         #Obtener ferlitianzate y agua
            #         aguaopt = Inv.historiaagua.Obtener(h+1)
            #         fertopt = Inv.historaifertilizante.Obtener(h+1)
            #         #Obtener lista drones
            #         ListaDronesResumen = Inv.historialdrones.Obtener(h+1)
                    
            #         print('\n---[Plan info]---')
            #         Planinfo.desplegar()
            #         print('---[Fin Plan info]---\n')

            #         print('\n---[Movimientos]---')
            #         Movmientos.desplegar()
            #         print('---[Fin Movimientos]---\n')



            #         #Datos Planes
            #         plan = doc.createElement('plan')
            #         plan.setAttribute('nombre',f'{Planinfo.nombre}')
            #         listaplanes.appendChild(plan)

            #         #Tiempo optimo
            #         tiempoOptimo = doc.createElement('tiempoOptimoSegundos')
            #         plan.appendChild(tiempoOptimo)
            #         txt= doc.createTextNode(f'{TiempooptimoInv}')
            #         tiempoOptimo.appendChild(txt)

            #         #aguaRequeridaLitros
            #         aguaRequerida = doc.createElement('aguaRequeridaLitros')
            #         plan.appendChild(aguaRequerida)
            #         txt= doc.createTextNode(f'{aguaopt}')
            #         aguaRequerida.appendChild(txt)

            #         #Fertilizante
            #         fertilizanteReq = doc.createElement('fertilizanteRequeridoGramos')
            #         plan.appendChild(fertilizanteReq)
            #         txt= doc.createTextNode(f'{fertopt}')
            #         fertilizanteReq.appendChild(txt)

            #         #Lista Eficiencia Drones
            #         efiDrones = doc.createElement('eficienciaDronesRegadores')
            #         plan.appendChild(efiDrones)

            #         #Dron
            #         for j in range(0,ListaDronesResumen.tamano()):
            #             DataDron = ListaDronesResumen.Obtener(j+1)
            #             Dron = doc.createElement('dron')
            #             efiDrones.appendChild(Dron)
            #             Dron.setAttribute('nombre',f'{DataDron.nombre}')
            #             Dron.setAttribute('litrosAgua',f'{DataDron.aguautilizada}')
            #             Dron.setAttribute('gramosFertilizante',f'{DataDron.fertilizanteutilizado}')

            #         #Lista instrucciones
            #         instrucciones = doc.createElement('instrucciones')
            #         plan.appendChild(instrucciones)

            #         #Tiempo
            #         for k in range(0,Movmientos.tamano()):
            #             movdata = Movmientos.Obtener(k+1)

            #             tiempo = doc.createElement('tiempo')
            #             tiempo.setAttribute('segundos',f'{movdata.tiemposeg}')
            #             instrucciones.appendChild(tiempo)

            #             #Movimiento
            #             listamovimientos = movdata.colamovimientos
            #             for l in range(0,listamovimientos.tamano()):
            #                 movi = listamovimientos.Obtener(l+1)
            #                 movimiento = doc.createElement('dron')
            #                 tiempo.appendChild(movimiento)
            #                 movimiento.setAttribute('nombre',f'{movi.nombre}')
            #                 movimiento.setAttribute('accion',f'{movi.accion}')

            
            

        except Exception as e:
            self.msg(f'!!! Error al segmentar_archivo_XML !!!\n',e)
        
    def creararchivoDOC(self):
        try:
            self.msg('Creando Doc and root')
            self.doc = Document()
            self.root = self.doc.createElement('archivoConfiguraciones')
            self.doc.appendChild(self.root)
        except Exception as e:
            self.msg("!!! Error al crear el archivo DOC!!!\n",e)
    
    def crear_archivo(self):
        try:
            contenido = self.doc.toprettyxml(indent=" ", encoding="UTF-8")
            with open(self.rutasalida, 'wb') as archivo:
                archivo.write(contenido)
            self.msg(">> Archivo creado o sobrescrito correctamente.\n")
        except Exception as e:
            self.msg(f'!!! Error al crear_archivo !!!\n',e)

    def msg(self, mensaje, extra=None):
        print(f'[SistemaLeerArchivosXML]>> {mensaje}')
        if extra != None and extra != '' and extra != ' ':
            print('\n>> ',extra)