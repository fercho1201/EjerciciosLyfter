my_list = ['4', 'hola', '10', '5.2']
def list_convertion(lst):
    new_list = []
    for i in lst: 
        try:
            i = int(i)
            new_list.append(f"{i} converted into:")
            new_list.append(i)
        except ValueError:
            new_list.append(f"{i} can't be converted to a number")
    new_list.insert(0, "Result: ")
    return new_list



print (list_convertion(my_list)) 