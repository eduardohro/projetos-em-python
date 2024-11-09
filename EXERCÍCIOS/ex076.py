### LISTA DE PREÇOS COM TUPLA ###

# Tupla contendo os produtos e seus preços
listagem = (
    'Lápis', 1.75, 
    'Borracha', 2, 
    'Caderno', 15.90, 
    'Estojo', 25, 
    'Trasnferidor', 4.20, 
    'Compasso', 9.99, 
    'Mochila', 120.32, 
    'Canetas', 22.30, 
    'Livro', 34.60)

# Exibe uma linha separadora
print('-'*30)
# Centraliza e imprime o título "LISTAGEM DE PREÇOS" em uma largura de 30 caracteres
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-'*30)

# Itera sobre a tupla 'listagem' de 2 em 2 elementos: produto (posição par) e preço (posição ímpar)
for i in range(0, len(listagem), 2):
    produto = listagem[i]  # O produto está na posição 'i'
    preco = listagem[i+1]  # O preço está na posição 'i + 1'

    # Imprime o produto e o preço formatados
    # Produto é alinhado à esquerda com 20 caracteres, e o preço é alinhado à direita com 2 casas decimais
    print(f'{produto:.<20}R$ {preco:>7.2f}')

print('-'*30)


### CURSO EM VIDEO ###

# listagem = (
#     'Lápis', 1.75, 
#     'Borracha', 2, 
#     'Caderno', 15.90, 
#     'Estojo', 25, 
#     'Trasnferidor', 4.20, 
#     'Compasso', 9.99, 
#     'Mochila', 120.32, 
#     'Canetas', 22.30, 
#     'Livro', 34.60)
# print('-' * 40)
# print(f'{"LISTAGEM DE PREÇOS":^40}')
# print('-' * 40)
# for pos in range(0, len(listagem)):
#     if pos % 2 == 0:
#         print(f'{listagem[pos]:.<30}', end='')
#     else:
#         print(f'R${listagem[pos]:>7.2f}')
# print('-' * 40)