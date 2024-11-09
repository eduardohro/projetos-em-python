### CONTANDO VOGAIS EM TUPLA ###

palavras = ('aprender', 'programar', 'linguagem', 'python', 'cursos', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
vogais = 'aeiouAEIOU'

for palavra in palavras:
    vogais_encontradas = []
    for letra in palavra:
        if letra in vogais and letra not in vogais_encontradas:
            vogais_encontradas.append(letra)

    print(f'Na palavra {palavra.upper()} temos: {" ".join(vogais_encontradas)}')
print()


### CURSO EM VIDEO ###

# palavras = ('aprender', 'programar', 'linguagem', 'python', 
#             'cursos', 'gratis', 'estudar', 'praticar', 
#             'trabalhar', 'mercado', 'programador', 'futuro')
# for palavra in palavras:
#     print(f'\nNa palavra {palavra.upper()} temos: ', end='')
#     for letra in palavra:
#         if letra.lower() in 'aeiou':
#             print(letra, end=' ')