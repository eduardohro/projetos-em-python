### CRIANDO UM MENU DE OPÇÕES ###

num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))

escolha = 0

while escolha != 5:
    escolha = int(input('''
O que você quer fazer com esses números?                  
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR 
[4] NOVOS NÚMEROS 
[5] SAIR DO PROGRAMA
                    
Sua escolha: '''))
    
    if escolha == 1:
        print(f'A soma entre {num1} + {num2} é {num1+num2}')
    elif escolha == 2:
        print(f'A multiplicação entre {num1} x {num2} é {num1*num2}')
    elif escolha == 3:
        if num1 > num2:
            maior = num1
        elif num2 > num1:
            maior = num2
            if num1 == num2:
                print('Os dois números são iguais!')
        print(f'Entre {num1} e {num2} o maior número é {maior}')
    elif escolha == 4:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    elif escolha == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida. Tente novamente!')
        
print('Programa encerrado.')
