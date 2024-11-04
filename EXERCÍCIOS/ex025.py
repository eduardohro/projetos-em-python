### PROCURANDO UMA STRING DENTRO DE OUTRA ###

nome = str(input('Seu nome tem (SILVA)? Digite seu nome completo: ')).strip().upper()

print(f'Seu nome tem Silva? {"SILVA" in nome}')