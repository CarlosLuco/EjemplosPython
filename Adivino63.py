# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:50:25 2020

@author: Emil Darat
"""
import platform
import os
import time

def limpiar_pantalla():
    time.sleep(6)
    print("\n" * 1)


numero = 0
print("Programa Adivino de números entre 0 y 63")
print("Escoja en su mente un número entre 0 y 63\n\n")
limpiar_pantalla()


print("Le mostraré secuencias de números, si su número está, escriba si\n")
print("1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63")
print("¿Está su numero?. Responda si/no\n")
respuesta = input()
if respuesta=="si":
    numero = numero + 1

print("2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31, 34, 35, 38, 39, 42, 43, 46, 47, 50, 51, 54, 55, 58, 59, 62, 63")
print("¿Está su numero?. Responda si/no\n")

respuesta = input()
if respuesta=="si":
    numero = numero + 2

print("4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31, 36, 37, 38, 39, 44, 45, 46, 47, 52, 53, 54, 55, 60, 61, 62, 63")
print("¿Está su numero?. Responda si/no\n")

respuesta = input()
if respuesta=="si":
    numero = numero + 4

print("8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31, 40, 41, 42, 43, 44, 45, 46, 47, 56, 57, 58, 59, 60, 61, 62, 63")
print("¿Está su numero?. Responda si/no\n")

respuesta = input()
if respuesta=="si":
    numero = numero + 8

print("16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63")
print("¿Está su numero?. Responda si/no\n")

respuesta = input()
if respuesta=="si":
    numero = numero + 16

print("32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, ")
print("¿Está su numero?. Responda si/no\n")

respuesta = input()
if respuesta=="si":
    numero = numero + 32

print("Espere un momento por favor\n\n")
limpiar_pantalla()

print("Su numero es el ", numero)