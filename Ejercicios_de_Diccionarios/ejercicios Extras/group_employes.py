employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "IT"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

departments_group = {}
for i in employees:
    name = i['name']
    department = i['department']
    
    if department not in departments_group:
        departments_group[department] = []
    
    departments_group[department].append(name)
    #creen una variable que guarda solamente el departamento y agrega el nombre del empleado que pertenezca a ese departamento a la lista.
    #departments_group[department].append(department), en este caso se el programa crea un directorio en base al departamento pero tambien agrega el diccionario completo del empleado. pero considero que es mas confuso por que hay mas informacion y ademas el nombre del departamento se repite dentro del diccionario.


print(departments_group)


    #  



