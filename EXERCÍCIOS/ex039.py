### ALISTAMENTO MILITAR ###

from datetime import date

sexo = int(input('''
[1] Feminino
[2] Masculino
Digite o número do seu sexo: '''))

if sexo == 1:
    print('\nVocê é mulher, não tem necessidade de você fazer o alistamento!\n')
elif sexo == 2:
    a = int(input('Digite o ano de seu nascimento: '))

    ano_atual = date.today().year
    idade = ano_atual - a
    ainda1 = 18 - idade
    ainda2 = idade - 18

    if idade < 18:
        print(f'\nVocê ainda tem {idade} anos e faltam {ainda1} anos para se alistar ao serviço militar!')
        ano = ano_atual + ainda1
        print(f'Seu alistamento será em {ano}.\n')
    elif idade == 18:
        print(f'\nVocê já tem {idade} anos, então está na hora de se alistar ao serviço militar!\n')
    else:
        print(f'\nVocê tem {idade} anos, já passou do tempo de alistamento com um atraso de {ainda2} anos! Vá se alistar ou pegar a reservista!')
        ano = ano_atual - ainda2
        print(f'Seu alistamento foi em {ano}.\n')
else:
    print('\nOpção inválida! Tente novamente!\n')