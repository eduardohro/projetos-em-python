### CALCULANDO DESCONTOS ###

preco = float(input('Qual o preço do produto? '))

novo = preco - (preco * 5 / 100) # Calculando novo preço com desconto

print(f'O valor a ser pago pelo produto com desconto de 5% é R$ {novo:.2f}')