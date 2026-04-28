def validar_nombre(nombre):
    if nombre.isdigit():
        raise ValueError('-El nombre no puede ser un número-')
    return nombre


def validar_edad(edad):
    try:
        edad_verificada = int(edad)
    except ValueError:
        raise ValueError('-Entrada de edad inválida-. Por favor ingrese un valor válido (debe ser un número).')
    
    if not (0 < edad_verificada <= 105):          
        raise ValueError("-La edad debe estar entre 0 y 105-")
    return edad_verificada             


def principal():
    try:
        nombre = input('Ingrese su nombre: ')
        edad = input('Por favor ingrese su edad: ')
        # validar_nombre(nombre)
        # validar_edad(edad)

        print(f'hola {validar_nombre(nombre)}, su edad es {validar_edad(edad)}') 

    except ValueError as ex:
        print(f'Ocurrió un error ---> {ex}')


if __name__ == "__main__":
    principal()