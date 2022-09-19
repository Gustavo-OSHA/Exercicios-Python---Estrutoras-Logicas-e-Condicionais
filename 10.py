"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes
formula( onde h corresponde a altura):
    - Homens: (72.7 * h ) - 58
    - Mulheres: (62.1 * h) - 44,7
"""
sexo = input('Iforme o seu sexo (homem ou mulher): ')
altura = float(input("Informe a sua Altura (exemplo 1.80):  "))
homem = (72.7 * altura) - 58
mulher = (62.1 * altura) - 44.7


if homem:
    print('Seu peso ideal é ', homem )
else:
    print('Seu peso ideal é ', mulher)    


