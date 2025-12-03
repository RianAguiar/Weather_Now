from django.shortcuts import render
from django.utils import timezone
import requests

from django.shortcuts import render
from django.utils import timezone
import requests

# --------------Classe responsável por buscar os dados na API

class WeatherService:
    API_KEY = '76c7584ee4406560c782fda32315a50c'
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
    def buscar_clima(self, cidade):
        url = f'{self.BASE_URL}?q={cidade}&appid={self.API_KEY}&lang=pt_br&units=metric'
        resposta = requests.get(url).json()
        return resposta


# Classe responsável por resolver qual ícone usar-------------
class IconResolver:
    ICONES = {
        'nublado': 'img/cloudy.png',
        'névoa': 'img/fog.png',
        'nuvens dispersas': 'img/cloudy.png',
        'algumas nuvens': 'img/cloudy.png',
        'pouca neve': 'img/snowy.png',
        'céu limpo': 'img/sun.png',
        'chuva leve': 'img/raining.png',
        'chuva moderada': 'img/raining.png',
        'trovoadas': 'img/lightingcloud.png',
    }

    def escolher_icone(self, descricao):
        for chave, caminho in self.ICONES.items():
            if chave in descricao:
                return caminho
        return ""  # caso nenhum ícone combine



# Controlador que monta o dicionário final de clima---------
class WeatherController:
    def __init__(self):
        self.service = WeatherService()
        self.icon_resolver = IconResolver()

    def obter_clima_formatado(self, cidade):
        resposta = self.service.buscar_clima(cidade)
        datahora = timezone.localtime(timezone.now())

        if resposta.get('cod') != 200:
            return {'erro': 'Cidade não encontrada'}

        descricao = resposta['weather'][0]['description']
        icone = self.icon_resolver.escolher_icone(descricao)

        return {
            'cidade': resposta['name'],
            'temperatura': resposta['main']['temp'],
            'icone': icone,
            'descricao': descricao.title(),
            'data': datahora.strftime('%d/%m/%Y'),
            'hora': datahora.strftime('%H:%M'),
        }

# VIEWS--------------------------------------------------------
def home(request):
    clima = None

    if 'cidade' in request.GET:
        cidade = request.GET['cidade']
        controller = WeatherController()
        clima = controller.obter_clima_formatado(cidade)

    return render(request, 'home.html', {'clima': clima})


def index(request):
    return render(request, 'index.html')
