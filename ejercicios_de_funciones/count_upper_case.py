def count_uppercase(my_string):
    uppper_count = 0
    lower_count = 0
    for character in my_string:
        if character.isupper():
            uppper_count += 1

        if character.islower():
            lower_count += 1

    return uppper_count, lower_count


my_string = 'Learning Is A Process, Not An Event'
upper, lower = count_uppercase(my_string)
print(f"Your string has {upper} upper case letters, and {lower} that are lowercase!")

upper, lower = count_uppercase('I Like To Learn With LYFTER ')
print (f'This phrase has {upper} upper case letters, and {lower} that are lowercase!')

