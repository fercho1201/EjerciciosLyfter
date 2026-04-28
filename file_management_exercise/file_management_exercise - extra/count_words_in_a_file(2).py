def count_words_in_file(path):
    word_counter = 0
    with open(path) as file:
        for line in file:
            line_list = line.split()
            word_counter += len(line_list)
    return f'This file has: {word_counter} words'

 
path = 'C:\\Users\\ferch\\Documents\\Academy_Python\\file_management_exercise\\test.txt'
print (count_words_in_file(path))
