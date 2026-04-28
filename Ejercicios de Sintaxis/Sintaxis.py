string = 'hey there'
string_2 = 'how are you'
print (string + string_2)
#si se puede hacer. answer was: hey therehow are you
string = 2
string_2 = 'como estas'
print (string + string_2)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

string = 'hola'
string_2 = 3
print (string + string_2)
#TypeError: can only concatenate str (not "int") to str

list = [1,2,3,4,5]
list_2 = ['hola', 'como', 'estas']
print (list + list_2)
# Si se puede hacer.

test = "hola"
print (string + list)
#TypeError: can only concatenate str (not "list") to str

float_ex = float(2.5)
int_ex = int(4)
print (float_ex + int_ex)
# Si se puede hacer.  answer was 6.5

bool_1 = True
bool_2 = False

print(bool_1+bool_2) 
# Si se puede hacer. anwer was 1