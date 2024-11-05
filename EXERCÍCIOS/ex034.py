### AUMENTOS MÚLTIPLOS ###

salario = float(input('Digite o salário do funcionário: R$'))

if salario <= 1250:
    novo = salario + (salario * 15 / 100) # Aumento de 15% no salario para valores menores ou iguais a R$ 1250,00
else:
    novo = salario + (salario * 10 / 100)# Aumento de 10% no salario para valores maiores a R$ 1250,00

print(f'''Com um salário de \033[31mR${salario:.2f}\033[m.
Totalizando em \033[32mR${novo:.2f}\033[m.''')