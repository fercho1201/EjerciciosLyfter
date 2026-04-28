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

def search_by_genre(games):
    genre_counts = {}
    for game in games:
        genre = game['Genre']

        if genre in genre_counts:
            genre_counts[genre] += 1
        else:
            genre_counts[genre] = 1
    sorted_genre_counts = dict(sorted(genre_counts.items()))
    return sorted_genre_counts


def display_game(games_genre):
    print("Genre Counts:")
    for genre, count in games_genre.items():
        print(f"{genre}: {count}")

def main():
    file_path = 'games_info.csv'
    games = read_csv_file(file_path)
    filtered_games = search_by_genre(games)
    display_game(filtered_games)

if __name__ == '__main__':
    main()