### VÁRIOS NÚMEROS COM FLAG ###

cont = soma = 0

while True:
    num = int(input('Digite um número [Digite 999 para encerrar!]: ')) 
    if num == 999:
        break

    soma += num
    cont += 1
    
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')