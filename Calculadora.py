#Calculadora

num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))

print("Operaciones ")

print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")

def suma(a,b):
    return a + b

opcion = input("Selecciona una operacion:")
match opcion:
    case "1":
        print(suma(num1,num2))
