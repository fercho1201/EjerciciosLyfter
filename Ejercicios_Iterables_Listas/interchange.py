my_list = [4, 3, 6, 1, 7]

new_list = [my_list[-1]] + my_list[1:-1] + [my_list[0]]

print (new_list)

my_list = [4, 3, 6, 1, 7]

new_list = [my_list[-1], *my_list[1:-1], my_list[0]]

print(new_list)



