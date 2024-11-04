### PRIMEIRA E ÚLTIMA OCORRÊNCIA DE UMA STRING ###

frase = str(input('Digite uma frase: ')).strip().upper()

print(f'\nA letra (a) apareceu {frase.count("A")} vezes na frase!')
print(f'Sua primeira aparição foi na posição {frase.find("A")+1}!')
print(f'Sua última aparição foi na posição {frase.rfind("A")+1 }!\n')