### MAIOR E MENOR VALORES NA LISTA ###

valores = list()

for i in range(5):
    valor = int(input(f'Digite um valor para a posição {i}: '))
    valores.append(valor)

print(f'Você digitou os valores {valores}')

maior = max(valores)
menor = min(valores)

posiçãomaior = [i for i, v in enumerate(valores) if v == maior]
posiçãomenor = [i for i, v in enumerate(valores) if v == menor]

print(f'O maior valor foi {maior} nas posições {posiçãomaior}')
print(f'O menor valor foi {menor} nas posições {posiçãomenor}')

### CURSO EM VIDEO ###

# listnum = []
# maior = menor = 0
# for c in range(0, 5):
#     listnum.append(int(input(f'Digite um valor para a Posição {c}: ')))
#     if c == 0:
#         maior = menor = listnum[c]
#     else:
#         if listnum[c] > maior:
#             maior = listnum[c]
#         if listnum[c] < menor:
#             menor = listnum[c]
# print('=-'*30)
# print(f'Você digitou os valores {listnum}')
# print(f'O maior valor digitado foi {maior} nas posições ', end='')
# for i, v in enumerate(listnum):
#     if v == maior:
#         print(f'{i}... ', end='')
# print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
# for i, v in enumerate(listnum):
#     if v == menor:
#         print(f'{i}... ', end='')