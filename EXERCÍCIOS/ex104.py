### VALIDANDO ENTRADA DE DADOS EM PYTHON ###

def leiaINT(msg):
    """
    -> Solicita ao usuário que insira um número inteiro.
    :param msg: A mensagem a ser exibida ao usuário.
    :return: O número inteiro digitado pelo usuário.
    """
    while True:
        n = input(msg).strip()
        if not n.isdigit():
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')
        else:
            return int(n)
        
n = leiaINT('Digite um número: ')
print(f'Você acabou de digitar o número {n}')


### VALIDANDO ENTRADA DE DADOS EM PYTHON, CURSO EM VIDEO ###

# def leiaINT(msg):
#     ok = False
#     valor = 0
#     while True:
#         n = str(input(msg))
#         if n.isnumeric():
#             valor = int(n)
#             ok = True
#         else:
#             print('\033[0;31ERRO! Digite um número inteiro válido!\033[m')
#         if ok:
#             break
#     return valor

# # Programa Principal
# n = leiaINT('Digite um número: ')
# print(f'Você acabou de digitar o número {n}')
