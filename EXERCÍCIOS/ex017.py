### CATETOS E HIPOTENUSA ###

from math import sqrt, pow

catop = float(input('Qual o valor do cateto oposto? '))
catad = float(input('Qual o valor do cateto adjacente? '))

h = sqrt(pow(catop, 2) + pow(catad, 2))

# Ou simplesmente importando 'hypot(catop, catad)'

print(f'Com um cateto oposto de {catop}')
print(f'e um cateto adjacente de {catad}')
print(f'O valor da hipotenusa vai medir {h:.2f}')