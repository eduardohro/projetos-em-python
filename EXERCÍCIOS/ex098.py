### FUNÇÃO DE CONTADOR ###

from time import sleep 

def contador(início, fim, passo):
    if passo == 0:
        passo = 1 # Evita erro de passo 0
    if início > fim and passo > 0:
        passo =- passo  # Ajusta para contagem regressiva

    print('-=' * 30)
    print(f'Contagem de {início} até {fim} de {abs(passo)} em {abs(passo)}') # abs() remove o sinal de negativo.
    for v in range(início, fim + (1 if passo > 0 else -1), passo):  # Inclui o fim
        print(f'{v} ', end='', flush=True) # `flush=True` garante que o texto é exibido imediatamente
        sleep(0.5)
    print('FIM!')


contador(início=1, fim=10, passo=1)
contador(início=10, fim=0, passo=-2)

print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(início, fim, passo)
