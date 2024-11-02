### SENO, COSSENO E TANGENTE ###

from math import sin, cos, tan, radians

a = int(input('Qual é o valor do ângulo? '))

print('-' * 24)

print(f'O Seno de {a}⁰ é {sin(radians(a)):.2f}')
print(f'O Coseno de {a}⁰ é {cos(radians(a)):.2f}')
print(f'A tangente de {a}⁰ é {tan(radians(a)):.2f}')

print('-' * 24)
