### DIVIDINDO VALORES EM VÁRIAS LISTAS ###

valores = []
pares = []
impares = []

while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-='*30)
print(f'A lista completa é {valores}')

for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
print('-='*30)

### CURSO EM VIDEO ###

# num = list()
# pares = list()
# impares = list()
# while True:
#     num.append(int(input('Digite um número: ')))
#     resp = str(input('Quer continuar? [S/N]: '))
#     if resp in 'Nn':
#         break
# for i, v in enumerate(num):
#     if v % 2 == 0:
#         pares.append(v)
#     elif v % 2 == 1:
#         impares.append(v)
# print('=-=' * 30)
# print(f'A lista completa é {num}')
# print(f'A lista de pares é {pares}')
# print(f'A lista de ímpares é {impares}')
# print('=-=' * 30)