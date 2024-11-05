### COMPARANDO NÚMEROS ###

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'\nO PRIMEIRO número: {num1}, é maior e o segundo: {num2}, é menor!\n')
elif num2 > num1:
    print(f'\nO SEGUNDO número: {num2}, é maior e o primeiro: {num1}, é o menor!\n')
else:
    print('\nO dois valores são IGUAIS!\n')