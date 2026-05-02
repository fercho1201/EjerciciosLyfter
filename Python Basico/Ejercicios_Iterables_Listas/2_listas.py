list1 = ['Practice ' , 'Perfect ', 'doesnot ', 'easier ','more ','we ','stronger ','more ']
list2 = ['Makes ','Life ','get ','or ','forgiving, ','get ','and ','resilient.']
list3 = []
for i in range(len(list1)):
    list3.append(list1[i])
    list3.append(list2[i])

sentence = ''.join(list3)
print(sentence)

