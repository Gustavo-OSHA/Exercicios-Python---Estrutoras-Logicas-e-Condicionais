"""
Leia o salario de um trabalhador e o valor da prestação de um emprestimo. Se a prestação for maior que 20% do salario imprima:
Emprestimo não concedido, caso contrario imprima: Emprestimo concedido
"""

salario = float(input('Informe o valor do salario: '))
limite = (salario * 0.20)
prestacao = float(input('Digite o valor da prestação que deseja pagar: '))

if prestacao > limite:
    print('Emprestimo não concedido')
else:
    print('Emprestimo aprovado')

