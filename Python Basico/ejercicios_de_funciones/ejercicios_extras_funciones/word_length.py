def character_counter(words, character):
    new_list = []
    for i in words:
        print (i)
        if len(i) > character:
            new_list.append(i)
    return new_list


word_list = ["mountain", "ocean", "lantern", "velocity","whisper", "galaxy", "ember", "crystal", "shadow", "meadow", "thunder", "horizon", "breeze", "cascade", "voyage"]
character = int(input("Input the minimum length of the characters to count in the words: "))

print(f"The words with at least '{character}' characters are: {character_counter(word_list, character)} ")