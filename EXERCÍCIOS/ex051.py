### PROGRESSÃO ARITMÉTICA ###

print('=' * 40)
print('\tPROGRESSÃO ARITMÉTICA')
print('=' * 40)

primeiro = int(input('\nDigite o 1º Termo: '))
razao = int(input('Digite a razão: '))

decimo = primeiro + (10 - 1) * razao 

for c in range(primeiro, decimo + razao, razao):
    print(f'{c} ', end = '→ ')
print('ACABOU!')