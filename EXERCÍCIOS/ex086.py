### MATRIZ EM PYTHON ###

matriz = []

for i in range(0, 3):
    linha = []

    for j in range(0, 3):
        valor = int((input(f'Digite o valor para a posição [{i}], [{j}]: ')))
        linha.append(valor)

    matriz.append(linha)

print('=-' * 30)
print('Matriz resultante:')
for linha in matriz:
    print(linha)

### CURSO EM VIDEO ###

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
# print('=-' * 30)
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#     print()
