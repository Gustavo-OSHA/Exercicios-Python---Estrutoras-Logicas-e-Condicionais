"""
Ler um numero inteiro. Se o numero lido for negativo, escreva a mensagem "Numero invalido". 
Se o numero for positivo, calcular o logarito deste numero
"""

import math

num = int(input('Digite um numero positivo: '))

if num < 0:
    print('Numero invalido')
else:
    print('O logaritmo de num é ', math.log10(num))    


"""
Para solucionar foi necessario importar a biblioteca MATH a sintaxe é 
import math

math.log10( x )

"""    