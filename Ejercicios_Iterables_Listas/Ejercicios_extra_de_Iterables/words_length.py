words = [ ]
long_words = [ ]
for i in range(5):  
    word = (input(f'type the word {i+1} to be added to the list: ')) 
    words.append(word)     
    if (len(word)) > 4:
        long_words.append(word)
print(f'The words that are bigger than 4 letters are: {long_words} and the list of all the words is: {words}')
