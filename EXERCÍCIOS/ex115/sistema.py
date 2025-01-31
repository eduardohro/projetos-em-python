from lib.interface import *
from lib.arquivo import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
       
    elif resposta == 3:
        
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)