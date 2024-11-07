### VALIDAÇÃO DE DADOS ###

s = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]

while s not in 'MF':
    s = str(input('\033[31mResposta inválida!\033[m'
                  '\nDigite o seu sexo apenas com \033[33m[M/F]\033[m: ')).upper()
    
if s == 'M':
    print('Sexo Masculino cadastrado com sucesso!')
else:
    print('Sexo Feminino cadastrado com sucesso!')