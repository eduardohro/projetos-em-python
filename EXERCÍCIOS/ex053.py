### DETECTOR DE PALÍNDROMO ###

frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'A frase "{frase}" fica de trás para frente "{inverso}".'
          '\nPortanto, a frase é um PALÍNDROMO!')
else:
    print(f'A frase "{frase}" fica de trás para frente "{inverso}".'
        '\nEssa frase não é um PALÍNDROMO!')