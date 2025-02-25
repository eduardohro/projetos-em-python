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


def resumo(n, aum=10, dim=13):
    print('-' * 36)
    print(f'{"RESUMO DO VALOR":^35}')
    print('-' * 36)

    print(f'Preço Analisado:    {moeda(n, True)}')
    print(f'Dobro do Preço:     {dobro(n, True)}')
    print(f'Metade do Preço:    {metade(n, True)}')
    print(f'{aum}% do Preço:       {aumentar(n, aum, True)}')
    print(f'{dim}% do Preço:       {diminuir(n, dim, True)}')

    print('-' * 36)

### CURSO EM VIDEO ###

# def aumentar(preco=0, taxa=0, formato=False):
#     """
#     -> Calcula o aumento de um determinado preço,
#     retornando o resultado com ou sem formatação.
#     :param preço: o preço que se quer reajustar.
#     :param taxa: qual é a porcentagem do aumento.
#     :param formato: quer a saída formatada ou não?
#     :return: o valor rreajustado, com ou sem formato.
#     """
#     res = preco + (preco * taxa/100)
#     return res if not formato else moeda(res)

# def metade(preco=0, formato=False):
#     res = preco / 2
#     return res if formato is False else moeda(res)

    
# def dobro(preco=0, formato=False):
#     res = preco * 2
#     return res if formato is False else moeda(res)


# def diminuir(preco=0, taxa=0, formato=False):
#     res = preco - (preco * taxa/100)
#     return res if not formato else moeda(res)


# def moeda(preco=0, moeda='R$'):
#     return f'R$ {moeda}{preco:>.2f}'.replace('.', ',')


# def resumo(preco=0, taxaa=10, taxar=5):
#     print('-' * 30)
#     print('RESUMO DO VALOR'.center(30))
#     print('-' * 30)
#     print(f'Preço analisado: \t{moeda(preco)}')
#     print(f'Dobro do preço: \t{dobro(preco, True)}')
#     print(f'Metade do preço: \t{metade(preco, True)}')
#     print(f'Com {taxaa} de aumento: \t{aumentar(preco, taxaa, True)}')
#     print(f'Com {taxar} de redução: \t{diminuir(preco, taxar, True)}')
#     print('-' * 30)
