list1 = ['first name', 'last name', 'age']
list2 = ['Cris', 'Ruiz', 36]
#just corrected my age and wanted to probe that the changes are beeing made correctly thru github.
dictionary = {}

for data in list1:
    dictionary[data] = list2[list1.index(data)]

print(dictionary)

print('hello world')
