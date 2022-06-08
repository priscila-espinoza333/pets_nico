from django.shortcuts import render
import requests

def index(request):
    
    api = "https://mindicador.cl/api"
    response = requests.get(api)
    json_request = response.json()
    ipc = json_request['ipc']['valor']
    fecha = json_request['ipc']['fecha']
    print('Retornar pagina galeria.html')
    return render(request, 'galeria.html', {'ipc': ipc, 'fecha': fecha})