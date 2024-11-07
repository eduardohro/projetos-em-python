### CONTAGEM REGRESSIVA ###

from time import sleep

print('-=-' * 9)
print('\tESTAÇÃO EDs')
print('=-=' * 9)

print('Começando a contagem em:')

for c in range(10, - 1, - 1):
    sleep(1)
    print(c)
sleep(0.5)

print('\n\033[32mDECOLAR!\033[m\n')