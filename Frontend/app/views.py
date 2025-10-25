from django.shortcuts import render
import requests


def index(request):
    return render(request, 'login.html')

def subirConfig(request):
    if request.method == 'POST':
        print('>subirconfig()')
        archivo = request.FILES.get('archivo')

        if not archivo:
            return render(request, 'subirConfig.html', {
                'banderaArchivo': False,
                'error': 'No se recibió ningún archivo'
            })

        # URL del backend Flask
        flask_url = 'http://127.0.0.1:4000/subirConfig'  

        try:
            # Enviar archivo al backend Flask
            files = {'archivo': (archivo.name, archivo.read(), 'application/xml')}
            response = requests.post(flask_url, files=files)

            # Mostrar éxito o error según respuesta
            if response.status_code == 200:
                return render(request, 'subirConfig.html', {'banderaArchivo': True})
            else:
                return render(request, 'subirConfig.html', {
                    'banderaArchivo': False,
                    'error': f'Error desde el backend ({response.status_code}): {response.text}'
                })

        except Exception as e:
            return render(request, 'subirConfig.html', {
                'banderaArchivo': False,
                'error': f'Error de conexión con backend Flask: {str(e)}'
            })

    else:
        return render(request, 'subirConfig.html')


def subirConsumos(request):
    return render(request, 'subirConsumos.html')

def panelOpciones(request):
    return render(request, 'panelOpciones.html')

def operacionesSistema(request):
    return render(request, 'OperacionesSistema.html')

def consultaPanel(request):
    return render(request, 'ConsultaPanel.html')

def crearNuevoDato(request):
    return render(request, 'CrearNuevo.html')

def selcliFacturacion(request):
    return render(request, 'SeleccionCliente.html')

def facturacion(request):
    return render(request, 'facturacion.html')

def ayuda(request):
    return render(request, 'ayuda.html')