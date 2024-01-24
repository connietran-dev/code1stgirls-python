import requests
from pprint import pprint

pokemon_number = input('What is the Pokemon\'s id?: ')

url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}/'

response = requests.get(url)
print(response)

pokemon = response.json()
# print(pokemon)
pprint(pokemon)

"""
Exercise 5.3: Get the height and weight of the Pokemon and print the output

Extension: Print the names of all of a specific Pokemon’s moves
"""

print(pokemon['height'])
print(pokemon['weight'])

list_moves = pokemon['moves']

for item in list_moves:
    print(item['move']['name'])
