### FUNÇÃO PARA FATORIAL ###

def fatorial(num=1, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número num. 
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            if c == 1:
                print(f'{c} = ', end='')  # Troca o 'x' por '=' no último número
            else:
                print(f'{c} x ', end='')  # Exibe 'x' para os outros números
    return f

print('-' * 20)
print(fatorial(5, show=True))


### FUNÇÃO PARA FATORIAL, CURSO EM VIDEO ###

# def fatorial(n, show=False):
#     """
#     -> Calcula o Fatorial de um número.
#     :param n: O número a ser calculado.
#     :param show: (Opcional) Mostrar ou não a conta.
#     :return: O valor do Fatorial de um número n. 
#     """
#     f = 1
#     for c in range(n, 0, -1):
#         if show:
#             print(c, end='')
#             if c > 1:
#                 print(' x ', end='')
#             else: 
#                 print(' = ', end='')
#         f *= c
#     return f

# # Programa Principal
# print(fatorial(5, show=True))