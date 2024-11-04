### VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO ###

cid = str(input('Sua cidade começa com (SANTO)? Digite o nome da cidade: ')).strip()

m = cid.upper()
m1 = m[0:5]

print('SANTO' in m1)