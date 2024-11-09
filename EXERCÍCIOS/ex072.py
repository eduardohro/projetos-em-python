### NÚMERO POR EXTENSO ###

numeros = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 
    'dezoito', 'dezenove', 'vinte'
)

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    while n < 0 or n > 20:  # Verifica se está fora do intervalo
        n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    
    print(f'Você digitou o número {numeros[n]}')

    # Pergunta se o usuário quer continuar
    while True:
        continuar = input('Quer continuar? [S/N]: ').strip().upper()
        if continuar in 'SN':
            break

    if continuar == 'N':
        break


### CURSO EM VIDEO ###

# cont = ('zero', 'um', 'dois', 'três', 'quatro', 
#         'cinco', 'seis', 'sete', 'oito', 'nove', 
#         'dez', 'onze', 'doze', 'treze', 'catorze', 
#         'quinze', 'dezesseis', 'dezessete', 'dezoito', 
#         'dezenove', 'vinte')

# while True:
#     # Solicita o número e verifica se está no intervalo válido
#     num = int(input('Digite um número entre 0 e 20: '))
    
#     if 0 <= num <= 20:
#         print(f'Você digitou o número {cont[num]}')
        
#         # Pergunta ao usuário se deseja continuar
#         while True:
#             continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]
#             if continuar in 'SN':
#                 break
#         if continuar == 'N':
#             break

#     else:
#         print('Tente novamente.', end='')
