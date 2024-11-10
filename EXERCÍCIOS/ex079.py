### VALORES ÚNICOS EM UMA LISTA ###

valores = []

while True:
    valor = int(input('Digite um valor: '))

    if valor in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(valor)
        print('Valor adicionado com sucesso...')

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 30)
print(f'Você digitou os valores {sorted(valores)}')

### CURSO EM VIDEO ###

# numeros = list()
# while True:
#     n = int(input('Digite um valor: '))
#     if n not in numeros:
#         numeros.append(n)
#         print('Valor adicionado com sucesso...')
#     else:
#         print('Valor duplicado! Não vou adicionar...')
#     r = str(input('Quer continuar? [S/N]: ')).strip()[0]
#     if r in 'Nn':
#         break
# print('-=' * 30)
# numeros.sort()
# print(f'Você digitou os valores {numeros}')