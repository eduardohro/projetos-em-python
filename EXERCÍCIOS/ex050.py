### SOMA DOS PARES ###

cont = s = 0

for c in range(1, 7):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        s += num 
        cont += 1
if s > 0:
    print(f'Você informou {cont} números pares e soma desses números é {s}')
else:
    print('Não foi digitado nenhum número par!')