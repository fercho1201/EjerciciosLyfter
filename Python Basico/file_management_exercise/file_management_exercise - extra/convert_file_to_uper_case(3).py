def count_words_in_file(path):
    with open(path) as file:
        content = file.read().upper()
    
    word_list = content.split()

    with open('output_uppercase_note.txt', 'w') as new_file:
        for word in word_list:
            new_file.write(word + '\n')

    return new_file
    
       
        

path = 'C:\\Users\\ferch\\Documents\\Academy_Python\\file_management_exercise\\test.txt'
print (count_words_in_file(path))

