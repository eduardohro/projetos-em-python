### SORTEANDO UM ITEM NA LISTA ###

from random import choice

nm1 = str(input('Digite o nome do 1º aluno: '))
nm2 = str(input('Digite o nome do 2º aluno: '))
nm3 = str(input('Digite o nome do 3º aluno: '))
nm4 = str(input('Digite o nome do 4º aluno: '))

alunos = choice([nm1, nm2, nm3, nm4])

print(f'O aluno sorteado foi o {alunos}!')