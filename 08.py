"""
Crie um programa que faca a conversao de Fahrenheit para Celsius e  vice-cersa
"""

def menu_inicial():
    print('Programa para Conversão de Temperaturas')
    print('1. Converter de Celsius para Fahrenheit')
    print('2. Converter de Fahrenheit para Celsius')

def cel_fahr():
    C = float(input('Entre com a temperatura em graus Celsius: '))
    F = C * (9 / 5) + 32
    print('Valor em Fahrenheit: {0}°F'.format(F))

def fahr_cel():
    F = float(input('Entre com a temperatura em graus Fahrenheit: '))
    C = (F - 32) * (5 / 9)
    print('Valor em Celsius: {0}°C'.format(C))

if __name__=='__main__':
    menu_inicial()
    escolha = input('Escolha o tipo de conversão que deseja realizar: ')

    if escolha == '1':
        cel_fahr()

    if escolha == '2':
        fahr_cel()

"""
Neste código criamos duas funções distintas de conversão: cel_fahr() e fahr_cel(), que realizam as conversões de celsius para fahrenheit e de fahrenheit para celsius,
respectivamente. Também criamos um menu de opções para que o usuário possa escolher o tipo de conversão desejada. Usamos a função input() para capturar o valor digitado
pelo usuário, e o convertemos para o tipo float antes de armazená-lo em uma variável de cálculo.

No programa principal simplesmente executamos o menu e chamamos a função escolhida pelo usuário.
"""