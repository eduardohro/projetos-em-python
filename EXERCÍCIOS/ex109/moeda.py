def metade(n, formt=False):
    resp = n / 2
    return moeda(resp, formt)


def dobro(n, formt=False):
    resp = n * 2
    return moeda(resp, formt)


def aumentar(n, pc, formt=False):
    pc = n * pc/100
    resp = pc + n
    return moeda(resp, formt)


def diminuir(n, pc, formt=False):
    pc = n * pc/100
    resp = n - pc
    return moeda(resp, formt)


def moeda(p, formt=False):
    if formt:
        return f'R$ {p:.2f}'.replace('.', ',')
    return p


### CURSO EM VIDEO ###

# def metade(preco=0, formato=False):
#     res = preco / 2
#     return res if formato is False else moeda(res)

    
# def dobro(preco=0, formato=False):
#     res = preco * 2
#     return res if formato is False else moeda(res)


# def aumentar(preco=0, taxa=0, formato=False):
#     res = preco + (preco * taxa/100)
#     return res if not formato else moeda(res)


# def diminuir(preco=0, taxa=0, formato=False):
#     res = preco - (preco * taxa/100)
#     return res if not formato else moeda(res)


# def moeda(preco=0, moeda='R$'):
#     return f'R$ {moeda}{preco:>.2f}'.replace('.', ',')
