#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

def sumar(valor1=0, valor2=0):
    return valor1 + valor2

def restar(valor1=0, valor2=0):
    return valor1 - valor2

def multiplicar(valor1=0, valor2=0):
    return valor1 * valor2

def dividir(valor1=0, valor2=1):
    if valor2 == 0:
        return "Error: No se puede dividir entre cero"
    return valor1 / valor2

def potencia(base=0, exponente=0):
    return base ** exponente

def raiz_cuadrada(valor=0):
    return math.sqrt(valor)

def mostrar_menu():
    print("** ::::::::::::::::::::::::: **")
    print(":: Calculadora de lesly jimenez ::")
    print("** ::::::::::::::::::::::::: **")
    print("-------------------------------")
    print("| Suma:             ->  1     |")
    print("| Resta:            ->  2     |")
    print("| Multiplicación:   ->  3     |")
    print("| División:         ->  4     |")
    print("| Potencia:         ->  5     |")
    print("| Raiz cuadrada:    ->  6     |")
    print("| Salir:            ->  7     |")
    print("-------------------------------")
    print("** ::::::::::::::::::::::::: **")
    print("\n")

def obtener_opcion():
    opcion = int(input("Seleccione una Opción... "))
    return opcion

def obtener_valores():
    valor1 = int(input("Ingrese su primer valor: "))
    valor2 = int(input("Ingrese su segundo valor: "))
    return valor1, valor2

def obtener_valor():
    valor = int(input("Ingrese un valor: "))
    return valor

def error_operacion():
    regresar = input("¿Quiere realizar una nueva operación [S/N]? ")
    return regresar

while True:
    mostrar_menu()
    opcion = obtener_opcion()

    if opcion == 1:
        print("\n** Entrando al módulo de Suma **")
        valor1, valor2 = obtener_valores()
        resultado_suma = sumar(valor1, valor2)
        print("El resultado de su suma es:", resultado_suma)
        nueva_operacion = error_operacion()
        if nueva_operacion.upper() != "S":
            break

    elif opcion == 2:
        print("\n** Entrando al módulo de Resta **")
        valor1, valor2 = obtener_valores()
        resultado_resta = restar(valor1, valor2)
        print("El resultado de su resta es:", resultado_resta)
        nueva_operacion = error_operacion()
        if nueva_operacion.upper() != "S":
            break

    elif opcion == 3:
        print("\n** Entrando al módulo de Multiplicación **")
        valor1, valor2 = obtener_valores()
        resultado_multiplicacion = multiplicar(valor1, valor2)
        print("El resultado de su multiplicación es:", resultado_multiplicacion)
        nueva_operacion = error_operacion()
        if nueva_operacion.upper() != "S":
            break

    elif opcion == 4:
        print("\n** Entrando al módulo de División **")
        valor1, valor2 = obtener_valores()
        resultado_division = dividir(valor1, valor2)
        print("El resultado de su división es:", resultado_division)
        nueva_operacion = error_operacion()
        if nueva_operacion.upper() != "S":
            break

    elif opcion == 5:
        print("\n** Entrando al módulo de Potencia **")
        base = obtener_valor()
        exponente = obtener_valor()
        resultado_potencia = potencia(base, exponente)
        print("El resultado de su potencia es:", resultado_potencia)
        nueva_operacion = error_operacion()
        if nueva_operacion.upper() != "S":
            break

    elif opcion == 6:
        print("\n** Entrando al módulo de Raiz Cuadrada **")
        valor = obtener_valor()
        resultado_raiz = raiz_cuadrada(valor)
        print("El resultado de su raiz cuadrada es:", resultado_raiz)
        nueva_operacion = error_operacion()
        if nueva_operacion.upper() != "S":
            break

    elif opcion == 7:
        break
