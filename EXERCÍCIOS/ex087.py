### MAIS SOBRE MATRIZ EM PYTHON ###

matriz = []
somap = somacol3 = 0

for i in range(0, 3):
    linha = []

    for j in range(0, 3):
        valor = int((input(f'Digite o valor para a posição [{i}, {j}]: ')))
        linha.append(valor)

    matriz.append(linha)

print('=-' * 30)
print('Matriz resultante:')
for linha in matriz:
    print(linha)

    for v in linha:
        if v % 2 == 0:
            somap += v

for linha in matriz:
    somacol3 += linha[2]

maior = max(matriz[1])

print('=-' * 30)
print(f'A soma dos valores pares é {somap}')
print(f'A soma dos valores da terceira coluna é {somacol3}')
print(f'O maior valor da segunda linha é {maior}')

### CURSO EM VIDEO ###

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# spar = mai = scol = 0
# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
# print('=-' * 30)
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#         if matriz[l][c] % 2 == 0:
#             spar += matriz[l][c]
#     print() 
# print('-=' * 30)
# print(f'A soma dos valores pares é {spar}')
# for l in range(0, 3):
#     scol += matriz[l][2]
# print(f'A soma dos valores da terceira coluna é {scol}')
# for c in range(0, 3):
#     if c == 0:
#         mai = matriz[1][c]
#     elif matriz[1][c] > mai:
#         mai = matriz[1][c]
# print(f'O maior valor da segunda linha é {mai}')