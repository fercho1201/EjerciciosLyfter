
def reverse_string(n):
    new_note = ''   
    for charcter in n:
        new_note = charcter + new_note
    return (new_note)

note = 'retfyl ni nrael ot ekil i'
print(reverse_string(note))


def reverse_string2(n):
    note = n[::-1]
    print (note)

reverse_string2('retfyl ni nrael ot ekil i')