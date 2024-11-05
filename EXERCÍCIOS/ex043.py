### ÍNDICE DE MASSA CORPORAL ###

peso = float(input('Digite seu peso kg(kilogramas): '))
altura = float(input('Digite sua altura m(metros): '))

imc = peso/(altura ** 2) # Calculando o IMC

print(f'Seu imc é \033[36m{imc:.2f}\033[m.', end=' ')

if imc < 18.5:
    print('Você está \033[36mAbaixo do peso!\033[m\n')
elif 18.5 <= imc < 25: # OUTRA FORMA DE REPRESENTAR.
    print('Você está no \033[32mPeso ideal!\033[m\n')
elif imc >= 25 and imc < 30:
    print('Você está no \033[33mSobrepeso!\033[m\n')
elif imc >= 30 and imc < 40:
    print('Você está na \033[35mObesidade!\033[m\n')
else:
    print('Você está na \033[31mObesidade mórbida!\033[m\n')