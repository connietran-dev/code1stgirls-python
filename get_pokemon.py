import requests
from pprint import pprint

pokemon_number = input('What is the Pokemon\'s id?: ')

url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}/'

response = requests.get(url)
print(response)

pokemon = response.json()
print(pokemon)
pprint(pokemon)

"""

"""

