### ANALISADOR COMPLETO ###

idades = maioridadehomem = totmulher20 = 0
nomevelho = ''

for p in range(1, 5):
    print(f'–––– {p}ª PESSOA ––––')

    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    idades += idade

    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

media = idades / 4
print(f'\nA média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.\n ')