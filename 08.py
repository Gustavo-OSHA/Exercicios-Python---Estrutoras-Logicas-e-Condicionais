"""
Faça um programa que leia 2 notas de um aluno, verifique se as nostas são validas e exiba na tela a media destas notas.
Uma nota valida de ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor valido, este 
fato deve ser informado ao usuario e o programa termina
"""

nota_1 = float(input('Digite a nota: '))
nota_2 = float(input('Digite a segunda nota: '))


def nota_valida(nota):
    if nota >= 0 and nota <= 10:
        return True
    else:
        return False  

def media(nota_1, nota_2):
    pontuacao = (nota_1 + nota_2) / 2
    print(f'A media é', pontuacao)

if __name__=='__main__':

    if (nota_valida(nota_1) and nota_valida(nota_2)):
        media(nota_1, nota_2)
    else:
        print("Pelo menos uma das notas digitadas não é valida. Tente novamente")    
   



    




