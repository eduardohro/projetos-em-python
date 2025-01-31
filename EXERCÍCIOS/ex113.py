### FUNÇÕES APROFUNDADAS EM PYTHON ###

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


def leiaFloat(msg):
    """
    -> Solicita ao usuário que insira um número real.
    :param msg: A mensagem a ser exibida ao usuário.
    :return: O número real digitado pelo usuário.
    """
    while True:
        try:
            n = input(msg).strip().replace(',', '.')
            if n == "":
                raise ValueError
            return float(n)
        except ValueError:
            print('\033[31mERRO! Digite um número real válido!\033[m')
        except KeyboardInterrupt:
            print('\033[31mnO usuário preferiu não informar os dados!\033[m')
            return 0.0


i = leiaINT('Digite um número Inteiro: ')
r = leiaFloat('Digite um número Real: ')
print(f'O número Inteiro digitado foi {i} e o Real foi {r}')


### FUNÇÕES APROFUNDADAS EM PYTHON, CURSO EM VIDEO ###

# def leiaINT(msg):
#     while True:
#         try:
#             n = int(input(msg))
#         except (ValueError, TypeError):
#             print('\033[31mERRO: Por favor, digite um número inteiro válido.\033[m')
#             continue
#         except (KeyboardInterrupt):
#             print('\033[31mUsuário preferiu não digitar esse número.\033[m')
#             return 0
#         else:
#             return n


# def leiaFloat(msg):
#     while True:
#         try:
#             n = float(input(msg))
#         except (ValueError, TypeError):
#             print('\033[31mERRO: Por favor, digite um número real válido.\033[m')
#             continue
#         except (KeyboardInterrupt):
#             print('\033[31mUsuário preferiu não digitar esse número.\033[m')
#             return 0
#         else:
#             return n

# num1 = leiaINT('Digite um número Inteiro: ')
# num2 = leiaFloat('Digite um número Real: ')
# print(f'O valor Inteiro digitado foi {num1} e o real foi {num2}')