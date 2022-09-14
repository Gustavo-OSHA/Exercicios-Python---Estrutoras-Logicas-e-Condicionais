"""
Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois forem numeros iguais,
imprima a mensagem Numeros Iguais
"""

num = int(input('Digite um numero: '))
num1 = int(input('Digite outro numero: '))

if num == num1:
    print('Numeros iguais por favor, digite numeros diferentes')
elif num > num1:
    print(num)  
else:
    print(num1)    