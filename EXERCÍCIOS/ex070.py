### ESTATÍSTICAS EM PRODUTOS ###

print('='*40)
print(f'{"LOJA SUPER BARATÃO":^40}')
print('='*40)

totcom = quant = prod1000 = prodbar = 0
nomeprodbar = ''

while True:
    
    produto = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o preço do produto: R$ '))

    quant += 1
    totcom += preco
    if preco > 1000:
        prod1000 += 1
    if quant == 1 or preco < prodbar: # SE O PRIMEIRO FOR O MAIS BARATO
        prodbar = preco # ENTÃO O PRODUTO RECEBE O PREÇO DO PRODUTO
        nomeprodbar = produto
    if preco == prodbar:
        nomeprodbar = produto

    print('='*30)

    while True:
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]

        if continuar in 'SN':
            break
        print('Entrada inválida. Por favor, digite apanes [S] para Sim ou [N] para Não.')
    
    print('='*30)

    if continuar == 'N':
        break

print('{:=^37}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi de R$ {totcom:.2f}.')
print(f'Temos {prod1000} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {nomeprodbar} que custa R$ {prodbar:.2f}.\n')