import csv


def read_csv_file(file_path):
    games = []

    with open(file_path, newline='') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            game = {
                "Name": row["Name"],
                "Genre": row["Genre"],
                "Developer": row["Developer"],
                "Rating -ESRB-": row["Rating -ESRB-"]
            }
            games.append(game)

    return games

def display_games(games):
    for index, game in enumerate(games, start=1):
        print(f"-- Game {index} --")
        for key, value in game.items():
            print(f"{key}: {value}")
        print() 

def main():
    file_path = "games_info.csv"
    games = read_csv_file(file_path)
    display_games(games)


if __name__ == "__main__":
    main()


import csv


def read_csv_file(file_path,):
    with open(file_path, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        counter = 1
        next(reader)
        for row in reader:
            print(f"--Game {counter}--")
            game = {
                'Name': row[0],
                'Genre': row[1],
                'Developer': row[2],
                'Rating -ESRB-': row[3]
            } 
            counter += 1
            for key, value in game.items():
                print(f"{key}: {value}")
            
    return 'Process completed successfully...!'

file_path = 'games_info.csv'
print(read_csv_file(file_path))