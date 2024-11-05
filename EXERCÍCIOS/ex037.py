### CONVERSOR DE BASES NUMÉRICAS ###

num = int(input('Digite um número inteiro: '))

print('''\nEscolha a base de conversão:
1 - Binário;
2 - Octal;
3 - Hexadecimal.''')
opção = int(input('Sua opção: '))

if opção == 1:
    print(f'{num} convertido para Binário é igual a {bin(num)[2:]}'
          '\n') # [2:] CORTA OS DOIS PRIMEIROS CARACTERES
elif opção == 2:
    print(f'{num} convertido para Octal é igual a {oct(num)[2:]}'
          '\n')
elif opção == 3:
    print(f'{num} convertido para Hexadecimal é igual a {hex(num)[2:]}'
          '\n')
else:
    print('\033[31mOpção inválida!\033[m')