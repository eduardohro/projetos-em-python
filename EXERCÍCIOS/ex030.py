### PAR OU ÍMPAR? ###

num = int(input('Digite um número: '))

ip = num % 2

print(f'O número {num} é PAR!' if ip == 0 else f'O número {num} é ÍMPAR!')