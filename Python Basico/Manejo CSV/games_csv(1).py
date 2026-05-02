import csv

def non_empty_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        else:
            print("Error: Input cannot be empty. Please enter a valid value.")

def get_games():
    continue_input = True 
    games = []
    while continue_input:
        name = non_empty_input('Enter the game title: ')
        genre = non_empty_input('Enter the game genre: ')
        developer = non_empty_input('Enter the game developer: ')
        rating = non_empty_input('Enter the game rating -ESRB-: ')

        games.append(
                    {
                    'Name': name,
                    'Genre': genre,
                    'Developer': developer,
                    'Rating -ESRB-': rating
                    })
            
        answer = non_empty_input("Add another? (y/n): ").strip().lower()
        if answer == 'n':
            print("Exiting....")
            continue_input = False
    return games





def write_games_csv_file(file_path, games, game_headers):
    with open(file_path, 'w', newline='') as new_file:
        write_new = csv.DictWriter(new_file, fieldnames=game_headers )
        write_new.writeheader()
        write_new.writerows(games)
    print("CSV file created succsesfully!")
    
def main():
    gamesheaders = (
    'Name',
    'Genre',
    'Developer',
    'Rating -ESRB-'
)
    games = get_games()
    write_games_csv_file('games_info(1).csv', games, gamesheaders)


if __name__ == "__main__":
    main()
