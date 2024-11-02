### SORTEANDO UMA ORDEM NA LISTA ###

from random import shuffle

nm1 = str(input('Digite o nome do 1º aluno: '))
nm2 = str(input('Digite o nome do 2º aluno: '))
nm3 = str(input('Digite o nome do 3º aluno: '))
nm4 = str(input('Digite o nome do 4º aluno: '))

alunos = [nm1, nm2, nm3, nm4]
shuffle(alunos)

print('A ordem de apresentação: ')
print(alunos)
