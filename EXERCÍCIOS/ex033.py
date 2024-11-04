### MAIOR E MENOR VALORES ###

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

# VERIFICANDO QUEM É O MENOR.
menor = a
if b < a and b > c:
    menor = b
if c < a and c < b:
    menor = c

# VERIFICANDO QUEM É O MAIOR.
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O maior número digitado foi \033[32m{maior}\033[m.')
print(f'O menor número digitado foi \033[31m{menor}\033[m.')