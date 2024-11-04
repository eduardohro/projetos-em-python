### ANO BISSEXTO ###

from datetime import date 

a = int(input('\nQual ano quer saber se é bissexto? Ou digite 0 para o ano atual: '))

if a == 0:
    a = date.today().year # SELECIONA O ANO ATUAL.
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'O ano de \033[32m{a}\033[m é BISSEXTO!')
else:
    print(f'O ano de \033[31m{a}\033[m não é BISSEXTO!')