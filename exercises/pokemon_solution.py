import requests

def poke_weight(name):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + name)
    quote_data = response.json()    
    return quote_data['weight']


poke_dict = {}


while True:
    name = input("Pokemon name: ")
    if name == 'done':
        print(poke_dict)
        break
    weight = poke_weight(name)
    poke_dict[name] = weight
    



# print(poke_weight('pikachu'))
# print(poke_weight('jigglypuff'))
# print(poke_weight('snorlax'))
