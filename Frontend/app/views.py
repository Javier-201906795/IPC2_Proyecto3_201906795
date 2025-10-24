from django.shortcuts import render
import requests


def index(request):
    return render(request, 'index.html')

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
