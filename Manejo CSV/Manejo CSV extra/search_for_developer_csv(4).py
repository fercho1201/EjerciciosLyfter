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

def search_by_developer(games):
    devinput = input("Enter the developer you want to search for: ").strip().lower()
    developer_list = {}
    for game in games:
        developer = game['Developer']
        if devinput in developer.lower():
           developer_list[developer] = developer_list.get(developer, []) + [game]
   
    return developer_list




def display_game(games_by_developer):
    if games_by_developer:
        for developer, games in games_by_developer.items():
            print(f"\nGames developed by: --{developer}--\n")
            print ('-' * 50)
            print ("Name | Genre | Developer | Rating -ESRB-")
            for game in games:
                print(f"{game['Name']} | {game['Genre']} | {game['Developer']} | {game['Rating -ESRB-']}")
    else:
        print("No games found for the specified developer.")
        

def main():
    file_path = 'games_info.csv'
    games = read_csv_file(file_path)
    filtered_games = search_by_developer(games)
    display_game(filtered_games)

if __name__ == '__main__':
    main()