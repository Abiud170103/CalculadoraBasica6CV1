#Calculadora

num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))

print("Operaciones ")

print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Módulo")

def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a, b):
    return a * b

def modulo(a,b):
    return a % b


opcion = input("Selecciona una operacion:")
match opcion:
    case "1":
        print(suma(num1,num2))
    case "2":
        print(resta(num1,num2))
    case "3":
        print(multiplicacion(num1, num2))
    case "5":
        print(modulo(a,b))
