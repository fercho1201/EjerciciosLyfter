import json 
import os  

def open_json_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        print("File not found.")
        return None
    
def print_json_data(data):
    if data is not None:
        counter = 0
        for pokemon in data:
            counter += 1
            print(f"---Pokemon No.: {counter}---")
            print(f"Name: {pokemon['name']['english']}")
            print(f"Level: {pokemon['level']}")
            print(f"Type: {', '.join(pokemon['type'])}")
            print("Base Stats:")
            for stat, value in pokemon['base'].items():
                print(f"  {stat}: {value}")
            print("-" * 21)
    else:
        print("No data to display.")   

def main():
    file_path = "./JSON/exercise.json"
    data = open_json_file(file_path)
    print_json_data(data)  

if __name__ == '__main__': 
    main()
