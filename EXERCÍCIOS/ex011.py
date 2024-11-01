### PINTANDO PAREDE ###

larg = float(input('Qual a largura da parede em metros? '))
alt = float(input('Qual a altura da parede em metros? '))

a = larg * alt # Calculando a área
l = a / 2 # Calculando total de litros necessários

print(f'Para pintar um área de {a:.2f}m², será necessário {l:.2f} litros de tinta')