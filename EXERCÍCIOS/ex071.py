### SIMULADOR DE CAIXA ELETRÔNICO ###

# NOTAS DE R$ 100,00 - R$ 50,00 - R$ 20,00 - R$ 10,00 - R$ 1,00

print('='*40)
print(f'{"BANCO ED":^40}')
print('='*40)

valor = int(input('Que valor você quer sacar? R$ '))

total = valor
ced = 100
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced +=1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break
        
print('='*40)
print('Volte sempre ao BANCO ED! Tenha um Bom dia!\n')