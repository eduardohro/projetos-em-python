### CUSTO DA VIAGEM ###

d = float(input('Qual a distância do trajeto em km: '))

vc1 = d * 0.50 # Cobra R$ 0,50 por Km para viagens de até 200Km
vc2 = d * 0.45 # E R$ 0,45 para viagens mais longas

if d <= 200:
    print(f'''Para um trajeto menor de {d}km, será cobrado R$0,50 por km.
Por tanto, o valor da passagem será R${vc1:.2f}.\n''')
else:
    print(f'''Para um trajeto maior de {d}km, será cobrado R$0,45 por km.
Por tanto, o valor da passagem será de R${vc2:.2f}.\n''')