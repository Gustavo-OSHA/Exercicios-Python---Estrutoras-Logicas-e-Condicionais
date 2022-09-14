"""
Faça um programa que leia 2 notas de um aluno, verifique se as nostas são validas e exiba na tela a media destas notas.
Uma nota valida de ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor valido, este 
fato deve ser informado ao usuario e o programa termina
"""

nota_1 = float(input('Digite a nota: '))
nota_2 = float(input('Digite a segunda nota: '))

def menu_notas():
    print('Qual a faixa de pontuação? ')
    print('1. De 1 a 10')
    print('2. Zero ')

def nota_valida():
    if nota_1 and nota_2 <=10:
        print('Nota valida')

def nota_invalida():
    if nota_1 or nota_2 <=0:
        print('Não é possivel fazer a recuperação')

def media():
    pontuacao = (nota_1 + nota_2) / 2
    print(f'A media é', pontuacao)

if __name__=='__main__':
    menu_notas()
    escolha = input('Escolha a nota: ')

    if escolha == '1':
        media()

    if  escolha == '2':
        nota_invalida()  


    




