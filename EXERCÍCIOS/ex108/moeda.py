def metade(n):
    return n / 2


def dobro(n):
    return n * 2


def aumentar(n, pc):
    pc = n * pc/100
    return pc + n


def diminuir(n, pc):
    pc = n * pc/100
    return n - pc


def moeda(p):
    return f'R$ {p:.2f}'.replace('.', ',')


### CURSO EM VIDEO ###

# def metade(preco=0):
#     res = preco / 2
#     return res

    
# def dobro(preco=0):
#     res = preco * 2
#     return res


# def aumentar(preco=0, taxa=0):
#     res = preco + (preco * taxa/100)
#     return res


# def diminuir(preco=0, taxa=0):
#     res = preco - (preco * taxa/100)
#     return res


# def moeda(preco=0, moeda='R$'):
#     return f'R$ {moeda}{preco:>.2f}'.replace('.', ',')
