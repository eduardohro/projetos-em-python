### FUNÇÃO QUE CALCULA ÁREA ###

def título(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


título(f'{"CONTROLE DE TERRENOS":^30}') 

def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg:.1f} x {comp:.1f} é de {a:.1f} m² ')
    
# Entrada dos dados
larg = float(input('LARGURA (M): '))
comp = float(input('COMPRIMENTO (M): '))

# Chamando a função
área(larg, comp)