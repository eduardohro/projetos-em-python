### PROGRESSÃO ARITMÉTICA V2.0 ###

print('-+' * 10)
print('Gerador de PA')
print('-+' * 10)

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

termo = primeiro
contador = 1

while contador <= 10:
    print(f'{termo} ', end= '→ ')
    termo += razao
    contador += 1

print('Acabou!')