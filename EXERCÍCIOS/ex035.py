### ANALISANDO TRIÂNGULO V1.0 ###

print('-=-' * 9)
print('ANALIZADOR DE TRIANGULOS')
print('-=-' * 9)

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(f'Com as medidas {r1}, {r2} e {r3}, \033[32mÉ SIM POSSÍVEL\033[m formar um triângulo!')
else:
    print(f'Com as medidas {r1}, {r2} e {r3}, \033[31mNÃO É POSSÍVEL\033[m formar um triângulo!')