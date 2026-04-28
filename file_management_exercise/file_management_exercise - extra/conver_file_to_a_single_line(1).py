def convert_file_to_single_line(path):
    new_list = []
    with open(path) as file:
        for line in file:
            new_list.append(line.strip())
    new_word = ' '.join(new_list)
    
    with open('output_for_this_exercise.txt', 'w') as new_file:
        new_file.write(new_word)
    return new_word



path = 'C:\\Users\\ferch\\Documents\\Academy_Python\\file_management_exercise\\Test.txt'
convert_file_to_single_line(path)
