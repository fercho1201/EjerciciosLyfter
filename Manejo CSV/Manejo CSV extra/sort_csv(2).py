import csv

def read_csv_file(file_path):
    games = []
    with open(file_path, 'r', newline = '') as csv_file:
        reader = csv.DictReader(csv_file)
        
        for row in reader: 
            game = {
                'Name': row['Name'],
                'Genre': row['Genre'],
                'Developer': row['Developer'],
                'Rating -ESRB-': row['Rating -ESRB-']
            } 
            games.append(game)
    return games

def search_by_rating(games):
    search =  input("Enter the rating you want to search for: --E for Everyone, T for Teen, M for Mature--, A for Adult 18+: ")
    filtered_games = []
    for game in games:
        if game['Rating -ESRB-'].lower() == search.lower():
            filtered_games.append(game)

    if not filtered_games:
            print(f"No games found with the rating '{search}'.")
    return filtered_games


def display_game(filtered_games):
    for i, game in enumerate(filtered_games, start=1):
        print(f"--Game {i}--")
        for key, value in game.items():
            print(f"{key}: {value}")
        print()

def main():
    file_path = 'games_info.csv'
    games = read_csv_file(file_path)
    filtered_games = search_by_rating(games)
    display_game(filtered_games)

if __name__ == '__main__':
    main()