### MAIOR E MENOR DA SEQUÊNCIA ###

pesos = []

for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa em (kg): '))
    pesos.append(peso)
    indice_maior_peso = pesos.index(max(pesos)) + 1
    indice_menor_peso = pesos.index(min(pesos)) + 1

print(f'\nO maior peso é da {indice_maior_peso}ª pessoa com {max(pesos)}kg')
print(f'O menor peso é da {indice_menor_peso}ª pessoa com {min(pesos)}kg\n')

### CURSO EM VIDEO ###

# maior = menor = 0

# for p in range(1, 6):
#     peso = float(input(f'Peso da {p}ª pessoa: '))
    
#     if p == 1:
#         maior = menor = peso
#     else:
#         if peso > maior:
#             maior = peso
#         if peso < menor:
#             menor = peso

# print(f'O maior peso lido foi de {maior}Kg')
# print(f'O menor peso lido foi de {menor}Kg')