# main.py
from sumar import sumar
from restar import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada


def menu():
    while True:
        print("\nCalculadora en Python")
        print("1. Sumar 2 números")
        print("2. Restar 2 números")
        print("3. Multiplicar 2 números")
        print("4. Dividir 2 números")
        print("5. Sumar N números")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("Resultado:", sumar(a, b))

        elif opcion == '2':
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("Resultado:", restar(a, b))

        elif opcion == '3':
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("Resultado:", multiplicar(a, b))

        elif opcion == '4':
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            try:
                print("Resultado:", dividir(a, b))
            except ZeroDivisionError:
                print("Error: no se puede dividir entre cero.")

        elif opcion == '5':
            numeros = input("Ingresa los números separados por coma: ")
            lista = [float(n) for n in numeros.split(',')]
            print("Resultado:", suma_avanzada(lista))

        elif opcion == '6':
            print("Saliendo de la calculadora.")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == '__main__':
    menu()
