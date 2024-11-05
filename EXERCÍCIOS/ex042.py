### ANALISANDO TRIÂNGULOS V2.0 ###

print('-=-' * 9)
print('ANALIZADOR DE TRIÂNGULO 2')
print('-=-' * 9)

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('\nCom essas medidas, pode se formar um TRIÂNGULO', end='')
    if r1 == r2 == r3:
        print(' EQUILÁTERO!\n')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print(' ISÓSCELES!\n')
    elif r1 != r2 != r3 != r1:
        print(' ESCALENO!\n')
else:
    print('\nCom essas medidas, não se pode formar um triângulo!\n')