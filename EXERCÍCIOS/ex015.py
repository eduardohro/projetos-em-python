### ALUGUEL DE CARROS ###

d = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram percorridos? '))

valorpagar = (d * 60) + (km * 0.15) # O carro custa R$ 60,00 por dia
                                    # E R$ 0,15 por km rodado
                                    
print(f'O total a pagar é de R$ {valorpagar:.2f}')