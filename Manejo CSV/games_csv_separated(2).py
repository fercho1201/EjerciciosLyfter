import csv


games = [
    {
    'Name': 'Grand Theft Auto IV',
    'Genre': 'Action',
    'Developer': 'Rockstar Games',
    'Rating -ESRB-': 'M'
    },
        {
    'Name': 'The Elder Scrolls IV',
    'Genre': 'PRG',
    'Developer': ' Bethesda',
    'Rating -ESRB-': 'M'
    },
        {
    'Name': 'Tony Hawks Pro Skater 2',
    'Genre': 'Sports',
    'Developer': 'Activision',
    'Rating -ESRB-': 'T'
    }
]

games_headers = (
    'Name',
    'Genre',
    'Developer',
    'Rating -ESRB-'
)

def write_csv_file(file_path, data, headers):
    with open(file_path, 'w', newline='') as new_file:
        write_new = csv.DictWriter(new_file, fieldnames=headers, delimiter= '\t') 
        write_new.writeheader()
        write_new.writerows(data)
    
    print("CSV file created succsesfully!")

write_csv_file('games_info(2).csv', games, games_headers)