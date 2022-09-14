"""
Leia um numero fornecido pelo usuario. Se esse numero for posistivo, calcule a raiz quadrada do número. Se o numero for negativo, mostre uma mensagem dizendo que 
o numero é invalido.
"""

numero = int(input("Informe um numero: "))

if numero > 0:
    print( numero ** (0.5)) 
else:
    print ("Numero invalido")    


"""
A raiz quadrada de um número nada mais é do que o número elevado à potência de 0,5. A função pow() em Python retorna o valor de um número
elevado a alguma potência especificada e pode ser usada para calcular a raiz quadrada de um número, conforme mostrado abaixo. 
O primeiro parâmetro da função pow() é a base e o segundo é o expoente.

Metodo pow()
print(pow(9,0.5))

Metodo com operador **
O operador ** executa a mesma função que o método pow. Podemos usá-lo para calcular a raiz quadrada de um número, conforme mostrado abaixo.
print(9 ** (0.5))
"""