### APROVANDO EMPRÉSTIMO ###

print('-=' * 5)
print('BANCO ED')
print('-=' * 5)

print('Seja bem vindo ao Banco ED.\n')

casa = float(input('Qual o valor da casa? R$ '))
sa = float(input('Qual o seu salário? R$ '))
a = int(input('Em quantos anos você quer pagar a casa? '))

vp = casa / (a * 12) # Valor da prestação
ps = vp * 100 / sa # Calculando o valor mínimo, sendo que ele não pode execeder 30% do salario da pessoa 

if ps > 30:
    print(f'''\n\033[31mInfelizmente você não pode finaciar essa casa!\033[m
Pois com um empréstimo de R${casa:.2f}
Com um salário de R${sa:.2f} e com o objetivo de pagar em {a} anos.
O valor das prestações iriam ficar em torno de R${vp:.2f} por mês.
Excedendo 30% do seu salário, ficando em torno de {ps:.0f}%.\n''')
elif ps <= 30:
    print(f'''\n\033[32mParabéns!\033[m
Com um emprestimo de R${casa:.2f}.
Com um salário de R${sa:.2f} e com o objetivo de pagar em {a} anos.
O valor das prestações ficará em torno de R${vp:.2f} por mês.
Sem exceder 30% do seu salário, ficando em torno de {ps:.0f}%.\n''')