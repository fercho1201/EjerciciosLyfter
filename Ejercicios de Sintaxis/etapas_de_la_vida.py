name= input('please type your name:')
lastname = input('please type your last name:')
age = int(input('please type your age:'))
if age <= 2:
    print(f'Hello {name} {lastname}, you are a baby!')
elif age >2 and age <=12:
    print(f"Hello {name} {lastname}, hey, nice, you're a kid!")
elif age >12 and age <=18:
    print(f"Hello {name} {lastname}, you're a teenager!")
elif age >15 and age <=22:
    print(f"Hello {name} {lastname}, you're a young adult!")
elif age >22 and age <=35:
    print(f"Hello {name} {lastname}, you're an adult!")
elif age >35 and age <=60:
    print(f"Hello {name} {lastname}, you're a senior citizen!")
else:
    print(f"Hello {name} {lastname}, you're an elder!")
