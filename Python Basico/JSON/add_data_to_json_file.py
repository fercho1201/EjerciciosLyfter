import json 
import os

def open_json_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        return []

def add_data_to_json_file(data):
    new_data = {
        "name": {
            "english": input("Enter the name of the new Pokemon: ")
        },
        "level": int(input("Enter the level of the new Pokemon: ")),
        "type": [t.strip() for t in input("Enter the type of the new Pokemon (separated by commas if multiple): ").split(',')],
        "base" : {
            "HP": int(input("Enter the HP of the new Pokemon: ")),
            "Attack": int(input("Enter the Attack of the new Pokemon: ")),
            "Defense": int(input("Enter the Defense of the new Pokemon: ")),
            "Sp. Attack": int(input("Enter the Sp. Attack of the new Pokemon: ")),
            "Sp. Defense": int(input("Enter the Sp. Defense of the new Pokemon: ")),
            "Speed": int(input("Enter the Speed of the new Pokemon: "))
        }
    }
    data.append(new_data)

def main():
    file_path = "./JSON/exercise.json"
    data = open_json_file(file_path)
    add_data_to_json_file(data)

    with open(file_path, "w") as file:
        json.dump(data, file, indent = 4)

    print ('New pokemon added successfully!')

if __name__ == '__main__':
    main()