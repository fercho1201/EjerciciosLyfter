def character_counter(t,c):
    count = 0
    for i in t:
        if i == c:
            count += 1
    return count

text = input("Input the text: ")
character = input("Input a character to count: ")
print(f"The character '{character}' appears {character_counter(text, character)} times in the text.")