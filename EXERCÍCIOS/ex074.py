### MAIOR E MENOR VALORES EM TUPLA ###

from random import randint

print(f'Os valores sorteados foram: ', end='')

cont = maior = menor = 0

for c in range(1, 6):
    vs = randint(1, 10)
    print(vs, end=' ')
    cont += 1

    if cont == 1:
        maior = menor = vs
    else:
        if vs > maior:
            maior = vs
        if vs < menor:
            menor = vs

print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')


### CURSO EM VIDEO ###

# from random import randint
# numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),)
# print('Os valores sorteados foram: ', end='')
# for n in numeros:
#     print(f'{n} ', end='')
# print(f'\nO maior valor sorteado foi {max(numeros)}')
# print(f'O menor valor sorteado foi {min(numeros)}')