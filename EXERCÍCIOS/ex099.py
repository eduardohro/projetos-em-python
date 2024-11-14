### FUNÇÃO QUE DESCOBRE O MAIOR ###

from time import sleep

def maior(* núm):
    
    print('-=' * 30)
    print('Analizando os valores passados...')
    
    maior = 0
    for i, v in enumerate(núm): 
        print(f'{v} ', end='', flush=True)
        sleep(0.5)   

        if i == 1:
            maior = v
        else:
            if v > maior:
                maior = v

    print(f'Foram informados {len(núm)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()