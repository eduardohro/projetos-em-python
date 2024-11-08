### ANÁLISE DE DADOS DO GRUPO ###

totpes18 = tothom = totmulher20 = idade = 0

while True:
        
    print('='*30)
    print(f'{"CADASTRE UMA PESSOA":^30}')
    print('='*30)

    idade = int(input('Idade: '))

    while True:

        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo in 'MF':
            break
        print('Entrada inválida. Por favor, digite [M] para masculino ou [F] para feminino')

    print('='*30)

    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

        if continuar in 'SN':
            break
        print('Entrada inválida. Por favor digite [S] para Sim ou [N] Não.')

    if idade >= 18:
        totpes18 += 1
    if sexo == 'M':
        tothom += 1
    if sexo == 'F' and idade < 20:
        totmulher20 += 1

    if continuar == 'N':
            break

print(f'\nTotal de pessoas com mais de 18 anos: {totpes18}.')
print(f'Ao todo temos {tothom} homens cadastrados.')
print(f'E temos {totmulher20} mulheres com menos de 20 anos.\n')