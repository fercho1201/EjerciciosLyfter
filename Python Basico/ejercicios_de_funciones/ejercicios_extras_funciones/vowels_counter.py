def character_counter(t):
    count = 0
    for i in t:
        if i in 'aeiouAEIOU':
            count += 1
    return f"There are {count} vowels in the text."

text = input("Input the text: ")
print(character_counter(text))
