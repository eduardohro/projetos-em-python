### CLASSIFICANDO ATLETAS ###

from datetime import date

a = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - a

if idade <= 9:
    print(f'Você tem {idade} anos, sua categoria é a MIRIM!\n')
elif idade <= 14:
    print(f'Você tem {idade} anos, sua categoria é a INFANTIL!\n')
elif idade <= 19:
    print(f'Você tem {idade} anos, sua categoria é a JUNIOR!\n')
elif idade <= 25:
    print(f'Você tem {idade} anos, sua categoria é a SÊNIOR!\n')
else:
    print(f'Você tem {idade} anos, sua categoria é a MASTER!\n')