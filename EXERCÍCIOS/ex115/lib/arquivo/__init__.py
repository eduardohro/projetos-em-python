from lib.interface import *


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mERRO ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()
        