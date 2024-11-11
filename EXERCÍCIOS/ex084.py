### LISTA COMPOSTA E ANÁLISE DE DADOS ###

pessoas = list()
dados = list()
pessmai = list()
pessmen = list()
totpes = pesomai = pesomen = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso [KG]: ')))

    pessoas.append(dados[:])
    dados.clear()
    totpes += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

for i, pessoa in enumerate(pessoas):
    if i == 1:
        pesomai = pesomen = pessoa[1]
    else:
        if pessoa[1] > pesomai:
            pesomai = pessoa[1]
        if pessoa[1] < pesomen:
            pesomen = pessoa[1]     

print('=-=' * 30)
print(f'Ao todo, você cadastrou {totpes} pessoas')

print(f'O maior peso foi de {pesomai:.1f} Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == pesomai:
        print(f'{pessoa[0]} ', end='')

print(f'\nO Menor peso foi de {pesomen}. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == pesomen:
        print(f'{pessoa[0]} ', end='')

### CURSO EM VIDEO ###

# temp = []
# princ = []
# mai = men = 0
# while True:
#     temp.append(str(input('Nome: ')))
#     temp.append(float(input('Peso: ')))
#     if len(princ) == 0:
#         mai = men = temp[1]
#     else:
#         if temp[1] > mai:
#             mai = temp[1]
#         if temp[1] < men:
#             men = temp[1]
#     princ.append(temp[:])
#     temp.clear()
#     resp = str(input('Quer continuar? [S/N]: '))
#     if resp in 'Nn':
#         break
# print('-=' * 30)
# print(f'Ao todo, você cadastrou {len(princ)} pessoas. ')
# print(f'O maior peso foi de {mai} Kg. Peso de ', end='')
# for p in princ:
#     if p[1] == mai:
#         print(f'[{p[0]}] ', end='')
# print()
# print(f'O menor peso foi de {men} Kg. Peso de ', end='')
# for p in princ:
#     if p[1] == men:
#         print(f'[{p[0]}] ', end='')
# print()