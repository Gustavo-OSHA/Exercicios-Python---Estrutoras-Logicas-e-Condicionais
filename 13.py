"""
Faça um algoritmo que calcule a media ponderada das notas de 3 provas. A primeira e segunda prova tem peso 1 e a terceira tem peso 2.
Ao final, mostrar a media do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou superior 
a 60 pontos
"""
nota_1 = int(input('Digite a primeira nota: '))
nota_2 = int(input('Digite a segunda  nota: '))
nota_3 = int(input('Digite a terceira nota: '))

nota = nota_3 * 2

media = (nota+nota_1+nota_2)/4
print(f'media = {media}')

if media >= 60:
    print('Aprovado')
else:
    print('Reprovado') 


"""
A média aritmética ponderada é calculada multiplicando cada valor do conjunto de dados pelo seu peso.

Depois, encontra-se a soma desses valores que será dividida pela soma dos pesos.
"""