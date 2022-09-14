"""
Escreva uma programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como diferença entre ambos.
"""

numero_1 = int(input('Digite um numero inteiro: '))
numero_2 = int(input('Digite outro numero inteiro: '))

if numero_1 > numero_2:
    print(numero_1)
    print(f'A diferença entre numero 1 e numero 2 é ', numero_1 - numero_2)
elif numero_1 == numero_2:
    print('Por favor digite numeros diferentes')    
if numero_1 < numero_2:
    print(numero_2)
    print(f'O valor do numero 1 é menor que o valor numero 2')
        
"""
Usei mais um elif para outra condição caso o numero fornecido seja igual , usuario fornecer outro numero 
"""