### BOLETIM COM LISTAS COMPOSTAS ###

alunos = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])    

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 30)
print(f'{"Nº.":<5} {"NOME":<7}   {"MÉDIA":>10}')
print('-' * 30)

for pos, aluno in enumerate(alunos):
    print(f'{pos:<5} {aluno[0]:<7} {aluno[2]:>10.1f}')
print('-' * 30)

while True:
    num = int(input('Mostrar notas de qual aluno? (999 interrope): '))

    for pos, aluno in enumerate(alunos):
        if num == pos:
            print(f'Notas de {aluno[0]} são {aluno[1]}')
    print('-' * 30)

    if num == 999:
        print('FINALIZANDO...')
        break

print('<<< VOLTE SEMPRE >>>')

### CURSO EM VIDEO ###

# ficha = list()
# while True:
#     nome = str(input('Nome: '))
#     nota1 = float(input('Nota 1: '))
#     nota2 = float(input('Nota 2: '))
#     media = (nota1 + nota2) / 2
#     ficha.append([nome, [nota1, nota2], media])
#     resp = str(input('Quer continuar? [S/N]: '))
#     if resp in 'Nn':
#         break
# print('-=' * 30)
# print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}')
# print('-=' * 30)
# for i, a in enumerate(ficha):
#     print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
# while True:
#     print('-' * 35)
#     opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
#     if opc == 999:
#         break
#     if opc <= len(ficha) - 1:
#         print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
# print('<<< VOLTE SEMPRE >>>')