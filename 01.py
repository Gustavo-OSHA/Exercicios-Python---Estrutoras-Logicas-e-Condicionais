"""
 In an imaginary country called Lisarb, all the people are very happy to pay their taxes because they know that doesn’t exist corrupt politicians and the taxes
 are used to benefit the population, without any misappropriation. The currency of this country is Rombus, whose symbol is R$.

 Salary                          Taxes
 from 0.00 to R$2.000.00         Without taxes
 from R$2.000.01 to R$3.000.00   8%
 from R$3.000.01 to R$4,500.00    18%
 more than R$4.500.00            28%

Read a value with 2 digits after the decimal point, equivalent to the salary of a Lisarb inhabitant.
Then print the due value that this person must pay of taxes, according to the table below.
"""


def menu_inicial():
    print('Informe a sua faixa Salarial')
    print('1. De 0 a 2.000.00')
    print('2. De 2.000.01 a 3.000.0')
    print('3. De 3.000.01 a 4.500.0')
    print('4. Mais que 4.500.01')

def sem_impostos():
    salario = float(input('Entre com o valor do salario: '))
    saldo = (salario * 1)
    print(f"Esta insento de impostos" , (saldo))

def imposto_oito_porcento():
    salario = float(input('Entre com o valor do salario: '))
    saldo = (salario * 0.8)
    print(f"Imposto de 8%, valor do desconto" , (saldo))

def imposto_dezoito_porcento():
    salario = float(input('Entre com o valor do salario: '))
    saldo = (salario * 0.18)
    print(f"Imposto de 18%, valor do desconto" , (saldo))

def imposto_vinteoito_porcento():
    salario = float(input('Entre com o valor do salario: '))
    saldo = (salario * 0.28)
    print(f"Imposto de 28%, valor do desconto" , (saldo))    

if __name__=='__main__':
    menu_inicial()
    escolha = input('Escolha a faixa salarial: ')

    if escolha == '1':
        sem_impostos()

    if escolha == '2':
        imposto_oito_porcento()
    
    if escolha == '3':
        imposto_dezoito_porcento()

    if escolha == '4':
        imposto_vinteoito_porcento()    