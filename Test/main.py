import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'fa25815b3d31e1dd276e5e1ec53b3d45'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "generate",
    "photo_id": 2
    }

#Создание покемона
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create) 
print(response_create.json)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)

body_name_change = {
    "pokemon_id": pokemon_id,
    "name": "New Name",
    "photo_id": 2
}

#Переименовать покемона
response_create = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name_change)
print(response_create.json)
print(response_create.text)

body_catch = {
    "pokemon_id": pokemon_id,
}

#Поймать в покебол
response_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_create.json)
print(response_create.text)
