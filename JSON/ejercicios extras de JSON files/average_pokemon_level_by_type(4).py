import json
import os 

def open_json_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        print("File not found.")
        return None
    
def calculate_average_level_by_type(data):
    if data is None:
        print('No data available')
        return None

    type_count = {}
    type_totals = {}

    for pokemon in data: 
        for t in pokemon['type']:
            if t not in type_count:
                type_totals[t] = 0
                type_count[t] = 0

            type_totals[t] += pokemon['level']
            type_count[t] += 1
    average = {}
    for t in type_totals:
        average[t] = type_totals[t] / type_count[t]
    return average
   
def main():
    file_path = "./JSON/exercise.json"
    data = open_json_file(file_path)
    average_level_by_type = calculate_average_level_by_type(data)
    if average_level_by_type is not None:
        for t, avg in average_level_by_type.items():
            print(f"{t} --> average level: {avg:.2f}")
    
if __name__ == '__main__':
    main()