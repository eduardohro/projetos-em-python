### EXTRAINDO DADOS DE UMA LISTA ###

valores = []
cont = 0

while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    cont += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print('==-' * 30)
print(f'Você digitou {cont} elementos.')

valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')

if 5 in valores:
    print(f'O valor 5 faz parte da lista! Na {valores.index(5)+1}ª posição.')
else:
    print(f'O valor 5 não faz parte da lista!')
print('==-' * 30)


### CURSO EM VIDEO ###

# valores = []
# while True:
#     valores.append(int(input('Digite um valor: ')))
#     resp = str(input('Quer continuar? [S/N]: ')).strip()[0]
#     if resp in 'Nn':
#         break
# print('=-=' * 30)
# print(f'Você digitou {len(valores)} elementos.')
# valores.sort(reverse=True)
# print(f'Os valores em ordem decrescente são {valores}')
# if 5 in valores:
#     print(f'O valor 5 faz parte da lista! Na posição {valores.index(5)}ª posição.')
# else:
#     print('O valor 5 não foi encontrado na lista!')
# print('=-=' * 30)