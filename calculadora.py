


def suma(a, b):
    return a + b    
    def resta(a, b):
    return a - b

def calculadora():
    print("Selecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    
    eleccion = input("Introduce el número de la operación que deseas realizar (1 o 2): ")
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))
    if eleccion == '1':
        print(f"La suma de {numero1} y {numero2} es: {suma(numero1, numero2)}")
    elif eleccion == '2':
        print(f"La resta de {numero1} y {numero2} es: {resta(numero1, numero2)}")
    else:
        print("Operación no válida. Por favor, selecciona 1 o 2.")
        calculadora()
