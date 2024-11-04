### RADAR ELETRÔNICO ###

v = float(input('Digite o valor da velocidade atingida pelo carro em KM/H: '))

m = (v - 80) * 7 # Multa de R$ 7,00 por cada Km acima do limite de 80Km/h

if v <= 80:
    print('\033[32mNão haverá multa! Velocidade dentro do limite.\033[m')
else:
    print(f'''\033[31mVelocidade acima do limite!
Multa calculada em \033[33mR$ {m:.2f}!\033[m''')