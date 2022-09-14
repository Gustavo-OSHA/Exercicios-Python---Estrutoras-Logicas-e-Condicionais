"""
Faca um programa que leia um número e , caso ele seja positivo, calcule e mostre:
    - O numero digitado ao quadrado
    - A raiz quadrada do numero digitado
    - Se o numero digitado for invalido, apresente uma mensagem na tela 
"""

numero_1 = int(input("Digite um numero: "))
raizq = (numero_1 * numero_1) ** 0.5

if numero_1 > 0:
    print(f'O valor do numero ao quadrado é ', numero_1 * numero_1 )
    print(f'A raiz quadrada é ', raizq)
else:
    print("Digite um numero válido")


"""
Metodo com operador **
A raiz quadrada de um número nada mais é do que o número elevado à potência de 0,5. Podemos usá-lo para calcular a raiz quadrada de um número, conforme mostrado abaixo.
print(9 ** (0.5))
Deve se lembrar que existe precedencia dos operadores para calculos matematicos 
"""    