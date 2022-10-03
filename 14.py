"""
A nota final de um estudante é calculada a partir de tres notas atribuidas entre o intervaldo de 0 ate 10, 
respectivamente, a um trabalho de laboratorio, a um avaliação semestral e a um exame final. A media das tres notas mencionadas
anteriormente obedece tais pesos: Trabalho de Laboratorio: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo com o resultado
, mostre na tela seo aluno esta reprovado(media entre 0 e 2.9), de recuperação ( entre 3 e 4.9) ou se foi aprovado.
Faça todas as verificações necessarias
"""


trabalho = float(input('Informe a nota do Trabalho: '))
avaliacao = float(input('Informe a nota da Avaliação: '))
prova = float(input('Informe a nota da Prova: '))

peso_trabalho = trabalho * 2
peso_avaliacao = avaliacao * 3
peso_prova = prova * 5
soma_peso = 10

media = peso_trabalho + peso_avaliacao + peso_prova / soma_peso

if media <= 0 or media <= 2.9:
    print('Reprovado', media)
if media <= 4.9:
    print('Recuperação', media)
else:
    print('Aprovado', media)
   
