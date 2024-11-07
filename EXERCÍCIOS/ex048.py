### SOMA ÍMPARES MÚLTIPLOS DE TRÊS ###

cont = s = 0

for c in range(1, 501, 2):
    impar = c % 3
    if impar == 0:
        cont += 1
        s += c

print(f'\nA soma de todos os {cont} valores impares múltiplos de 3 de 1 até 500 é {s}\n')