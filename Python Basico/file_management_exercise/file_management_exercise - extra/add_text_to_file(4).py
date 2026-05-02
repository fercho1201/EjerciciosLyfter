def add_text_to_file():
    new_text = input('please add the text you like to add to the note: ')
    with open('file_for_this_exercise.txt', 'a') as new_file:
        new_file.write(new_text + ' ') #no sabia si el texto se tenia que escribir en la misma linea pero usando un espacio o tenia que hacer que el programa guarde el texto nuevo en otra linea, en todo caso solo seria necesario cambiar el ' ' y escribir el comando que da una linea nueva '\n'

    print ('text added successfully.') 

add_text_to_file()

 