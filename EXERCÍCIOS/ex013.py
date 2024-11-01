### REAJUSTE SALARIAL ###

salario = float(input('Qual o salário do funcionário? R$'))

aumento = salario * 15 / 100

print(f'O funcionário com o salário de R$ {salario:.2f}')
print(f'Terá um aumento de 15% resultando em R$ {aumento:.2f}')
print(f'No total receberá cerca de R$ {salario + aumento}')