def leiaINT(msg):
    """
    -> Solicita ao usuário que insira um número inteiro.
    :param msg: A mensagem a ser exibida ao usuário.
    :return: O número inteiro digitado pelo usuário.
    """
    while True:
        try:
            n = input(msg).strip()
            if n == "":
                raise ValueError
            return int(n)
        except ValueError:
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não informar os dados!\033[m')
            return 0


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha()) 
        

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaINT('\033[32mSua Opção: \033[m')
    return opc
