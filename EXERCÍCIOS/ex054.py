### GRUPO DA MAIORIDADE ###

from datetime import date 

anoatual = date.today().year
totmaior = totmenor = 0

for pessoas in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {pessoas}ª pessoa: '))

    idade = anoatual - ano

    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
        
print(f'\nAo todo tivemos {totmaior} pessoas maiores de idade.')
print(f'E também tivemos {totmenor} pessoas menores de idade.\n')