import json
import os

def open_json_file(file_path): 
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        return [] 
    
def search_pokemon_by_type(data):
    search_type = input("Enter the type of the Pokemon you want to search for: ")
    found_pokemon = [] 
    for pokemon in data:
        if search_type.lower() in [t.lower() for t in pokemon['type']]:
            found_pokemon.append(pokemon)
    return found_pokemon

def display_pokemon_info(found_pokemon):
    if found_pokemon:
        print(f"Found {len(found_pokemon)} Pokemon(s) of the specified type:")
        print(' ')
        for pokemon in found_pokemon:
            print(f"Name: {pokemon['name']['english']}")
            print(f"Level: {pokemon['level']}")  
            print(f"Type: {', '.join(pokemon['type'])}")
            print ("-" * 20)
    else:
        print("Pokemon not found in the file.") 


def main():
    file_path = "./JSON/exercise.json"
    data = open_json_file(file_path) 
    found_pokemon = search_pokemon_by_type(data)
    display_pokemon_info(found_pokemon)

if __name__ == '__main__':
    main()