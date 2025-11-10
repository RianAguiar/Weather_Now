from django.shortcuts import render
from django.utils import timezone

import requests

def home(request):
    clima = None
    if 'cidade' in request.GET:
        cidade = request.GET['cidade']
        api_key = '76c7584ee4406560c782fda32315a50c'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br&units=metric'
        resposta = requests.get(url).json()
        datahora = timezone.localtime(timezone.now())
        if resposta.get('cod') == 200:
            clima = {
                'cidade': resposta['name'],
                'temperatura': resposta['main']['temp'],
                'descricao': resposta['weather'][0]['description'],
                'icone': resposta['weather'][0]['icon'],
                'data': datahora.strftime('%d/%m/%Y'),
                'hora': datahora.strftime('%H:%M'),
            }
        else:
            clima = {'erro': 'Cidade não encontrada 😢'}
    
    return render(request, 'home.html', {'clima': clima})