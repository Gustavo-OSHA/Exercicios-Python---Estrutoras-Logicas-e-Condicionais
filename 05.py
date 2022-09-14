"""
Faça um programa que receba um numero inteiro e verifique se este numero é par ou ímpar
"""

numero = int(input('Digite um numero inteiro: '))
if (numero%2) == 0:
    print('O numero', numero , 'é par')
else:
    print('O número', numero , 'é impar')  


"""
Para saber se um número é par ou ímpar, basta dividir ele por 2.
Se for par, o resto é sempre 0, não sobra nada.
Já se for ímpar, vai sempre ter resto 1.
Então para resolver utilizei o operador % que verfica o resto da divisão 
"""