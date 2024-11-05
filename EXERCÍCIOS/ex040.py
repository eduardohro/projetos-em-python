### AQUELE CLÁSSICO DA MÉDIA ###

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

me = (nota1 + nota2) / 2

print(f'\nCom as notas {nota1:.1f} e {nota2:.1f}. Sua média é de {me:.1f}.')
if me <= 5:
    print('\nEstá abaixo da média de 5.0. Portanto, está \033[31mREPROVADO!\033[m\n')
elif 7 > me > 5:
    print('\nEstá entre 5.0 e 6.9. Portanto, está de \033[33mRECUPERAÇÃO!\033[m\n')
elif me >= 7.0:
    print('\nEstá acima da média de 5.0. Portanto, está \033[32mAPROVADO!\033[m\n')