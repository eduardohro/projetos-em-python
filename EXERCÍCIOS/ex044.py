### GERENCIADOR DE PAGAMENTOS ###

from time import sleep
print('\n', '=' * 12, 'LOJAS PCsBREDU', '=' * 12)
print('{:-^40}'.format(' Artigos de informática ')) # OUTRA FORMA DE CENTRALIZAR

valor = float(input('\nQual o valor das compras: R$ '))
print('\n\tFORMA DE PAGAMENTO')
print('''\n1 - À vista/cheque com 10% de desconto;
2 - À vista no cartão com 5% de desconto;
3 - Em até 2x no cartão sem juros;
4 - Em 3x ou mais no cartão com 20% de juros.''')
es = int(input('\nEscolha uma forma de pagamento acima de acordo com a numeração: '))

if es == 4:
    print('PROCESSANDO...')
else:
    print('CALCULANDO...')
sleep(2)
if es == 1:
    desconto1 = valor * 10 / 100
    print(f'''\nVocê escolheu a 1ª opção.
Portanto, ganhará um desconto de 10% no valor de R${desconto1:.2f}.
No total sua compra irá custar em torno de R$ {valor - desconto1:.2f}.\n''')
elif es == 2:
    desconto2 = valor * 5 / 100
    print(f'''\nVocê escolheu a 2ª opção.
Portanto, ganhará um desconto de 5% no valor de R${desconto2:.2f}.
No total sua compra irá custar em torno de R$ {valor - desconto2:.2f}.\n''')
elif es == 3:
    duasvezes = valor / 2
    print(f'''\nVocê escolheu a 3ª opção.
Portanto, pagará em 2x no cartão no valor de R$ {duasvezes:.2f} sem juros.\n''')
elif es == 4:
    totalparc = int(input('\nQuantas parcelas: '))
    print('CALCULANDO...')
    sleep(2)

    parcela = valor / totalparc
    vinte = valor * 20 / 100

    print(f'''\nSua compra ficará no valor de R$ {parcela:.2f} em {totalparc} vezes.
Com o juros de 20% no valor de R$ {vinte:.2f}.
Totalizando em R$ {valor + vinte:.2f} no total com juros.\n''')
else:
    print('\033[31mEssa opção não existe!\033[m\n')