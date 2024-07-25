import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'fa25815b3d31e1dd276e5e1ec53b3d45'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

def test_status_code():
    response = requests.get('https://api.pokemonbattle.ru/v2/trainers')
    assert response.status_code == 200

def test_part():
    response_get = requests.get('https://api.pokemonbattle.ru/v2/trainers', params = {'trainer_id': '4717'})
    assert response_get.json()["data"][0]['trainer_name'] == 'Кейра Мец'