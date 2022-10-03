"""
Faca um programa que mostre ao usuario um menu com 4 opções de operações matematicas ( as basicas).
o usuario escolhe uma das opçoes e o se programa então pede dois valores numericos e realiza a operação,
mostrando o resultado e saindo
"""

base_maior = float(input('Digite um numero: '))
base_menor = float(input('Digite mais um numero: '))
altura = float(input('Digite uma altura: '))

if base_maior <= 0 or base_menor <= 0:
     print('Digite um valor maior que zero')
if base_maior < base_menor:
     print('Base maior tem que ser maior que Base menor ')     
else:
     Area = ((base_maior + base_menor) * altura) / 2
     print('A area do Trapezio é: ' + str(Area))
       
"""
Para o print do resultado , realizei a conversão do float para string
"""
