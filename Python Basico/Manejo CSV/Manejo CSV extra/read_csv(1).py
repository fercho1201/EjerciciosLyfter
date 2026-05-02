import csv


def read_csv_file(file_path):
    games = []
    with open(file_path, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        
        for row in reader: 
            game = {
                'Name': row[0],
                'Genre': row[1],
                'Developer': row[2],
                'Rating -ESRB-': row[3]
            } 
            games.append(game)    
    return games

def display_game(games):
    for i, game in enumerate(games, start=1):
        print(f"--Game {i}--")
        for key, value in game.items():
            print(f"{key}: {value}")
        print()

def main():
    file_path = 'games_info.csv'
    games = read_csv_file(file_path)
    display_game(games)

if __name__ == "__main__":
    main()