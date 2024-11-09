### ANÁLISE DE DADOS EM EM TUPLA ###

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o último número: '))

numeros = (num1, num2, num3, num4)
print(f'Você digitou os valores {numeros}')

cont = numeros.count(9)
print(f'O valor 9 apareceu {cont} vezes')


if 3 in numeros:
    numero = 3
    posicao = numeros.index(numero) + 1 
    print(f'O valor 3 apareceu na {posicao}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print('Os valores pares digitados foram: ', end='')
for num in numeros:
    if num % 2 == 0:
        print(f'{num}', end=' ')


### CURSO EM VIDEO ###

# num = (int(input('Digite um número: ')),
#        int(input('Digite outro número: ')),
#        int(input('Digite mais um número: ')),
#        int(input('Digite o último número: ')),)
# print(f'Você digitou os valores {num}')
# print(f'O valor 9 apareceu {num.count(9)} vezes')
# if 3 in num:
#     print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
# else: 
#     print('O valor 3 não foi digitado em nunhuma posição')
# print('Os valores pares digitados foram ', end='')
# for n in num:
#     if n % 2 == 0:
#         print(n, end=' ')