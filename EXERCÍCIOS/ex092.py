### CADASTRO DE TRABALHADOR EM PYTHON ###

from datetime import date

trabalhador = dict()

trabalhador['nome'] = str(input('Nome: '))
anonas = int(input('Ano de Nascimento: '))
trabalhador['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

trabalhador['idade'] = date.today().year - anonas

if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: R$ '))

    trabalhador['aposentadoria'] = trabalhador['contratação'] - anonas + 35

    print('-=' * 30)
    print(f'nome tem valor {trabalhador["nome"]}')
    print(f'idade tem o valor {trabalhador["idade"]}')
    print(f'ctps tem valor {trabalhador["ctps"]}')
    print(f'contratação tem valor {trabalhador["contratação"]}')
    print(f'salário tem o valor {trabalhador["salario"]}')
    print(f'aposentadoria tem o valor {trabalhador["aposentadoria"]}')
else:
    print('-=' * 30)
    print(f'nome tem valor {trabalhador["nome"]}')
    print(f'idade tem o valor {trabalhador["idade"]}')
    print(f'ctps tem valor {trabalhador["ctps"]}')

### CURSO EM VIDEO ###

# from datetime import datetime
# dados = dict()
# dados['nome'] = str(input('Nome: '))
# nasc = int(input('Ano de Nascimento: '))
# dados['idade'] = datetime.now().year - nasc
# dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
# if dados['ctps'] != 0:
#     dados['contratação'] = int(input('Ano de Contratação: '))
#     dados['salários'] = float(input('Salário: R$ '))
#     dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
# print('-+' * 30)
# for k, v in dados.items():
#     print(f'  - {k} tem o valor {v}')