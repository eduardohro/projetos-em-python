### UNINDO DICIONÁRIOS E LISTAS ###

pessoa = dict()
grupo = list()
soma = 0

while True:
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]: ')).strip().upper()[0]

        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))

    grupo.append(pessoa.copy())

    cont = ' '
    while cont not in 'SsNn':
        cont = str(input('Quer continuar? [S/N]: ')).strip()[0]
    if cont in 'Nn':
        break

print('-=' * 30)

print(f'- O grupo tem {len(grupo)} pessoas.')

for pessoa in grupo:
    soma += pessoa['idade'] 
media = soma / len(grupo)
print(f'- A média de idade é de {(media):.2f} anos.')

print('- As mulheres cadastradas foram: ', end='')
for pessoa in grupo:
    if pessoa['sexo'] in 'Ff':
        print(f'{pessoa["nome"]}', end=' ')
        
print('\n- Lista das pessoas que estão acima da média:')
for pessoa in grupo:
    for k, v in pessoa.items():
        if pessoa['idade'] > media:
            print(f'\n{k} = {v}', end='; ')

print('\n<< ENCERRADO >>')

### CURSO EM VIDEO ###

# galera = list()
# pessoa = dict()
# soma = média = 0
# while True:
#     pessoa.clear()
#     pessoa['nome'] = str(input('Nome: '))
#     while True:
#         pessoa['sexo'] = str(input('Sexo: [M/F]: ')).upper()[0]
#         if pessoa['sexo'] in 'MF':
#             break
#         print('\033[31mERRO!\033[m Por favor, digite apenas M ou F.')
#     pessoa['idade'] = int(input('Idade: '))
#     soma += pessoa['idade']
#     galera.append(pessoa.copy())
#     while True:
#         resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
#         if resp in 'SN':
#             break
#         print('\033[31mERRO!\033[m Por favor, digite apenas S ou N.')
#     if resp == 'N':
#         break
# print('-=' * 30)
# print(f'- Ao todo temos {len(galera)} pessoas cadastradas.')
# média = soma / len(galera)
# print(f'- A média de idade é de {média:5.2f} anos.')
# print('- As mulheres cadastradas foram ', end='')
# for p in galera:
#     if p['sexo'] in 'Ff':
#         print(f'{p["nome"]} ', end='')
# print()
# print('- Lista das pessoas que estão acima da média:')
# for p in galera:
#     if p['idade'] >= média:
#         print('     ', end='')
#         for k, v in p.items():
#             print(f'{k} = {v}; ', end='')
#         print()
# print('<< ENCERRADO >>')