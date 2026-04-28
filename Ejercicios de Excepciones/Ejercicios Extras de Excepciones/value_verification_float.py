def list_convertion(lst):
    new_list = []
    total_sum = 0
    for i in lst: 
        try:
            i = float(i)
            new_list.append(f"{i} added correctly")
            total_sum += i
        except ValueError:
            new_list.append(f"invalid element: {i}")
            
    new_list.append(f"Total sum: {total_sum}")
    return new_list


my_list = ['10', 'apple', '5.5', '3', 'n/a']
print (list_convertion(my_list))   