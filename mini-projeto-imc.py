# O PROGRAMA ABAIXO FOI DESENVOLVIDO A PARTIR DE UM ROTEIRO DE UM PORTIFÓLIO
# DA FACUDALDE [UNOPAR - PARAUAPEBAS/PA], QUE TRATA-SE DO CÁCULO IMC.
# COMO COMPLEMENTO FOI ADICIONADO DUAS BIBLIOTECAS PARA MANIPULAÇÃO E EXIBIÇÃO DE DADOS.
# ALÉM DE CONDIÇÕES ANINHADAS PARA AJUDAR NA ANÁLISE DOS DADOS.

import pandas as pd # BIBLIOTECA PARA ANÁLISE E MANIPULAÇÃO DE DADOS
from tabulate import tabulate # BIBLIOTECA PARA FORMATAR E EXIBIR DADOS TABULARES DE FORMA LEGÍVEL

print('=' * 50)
print('\t ÍNDICE DE MASSA CORPORAL (IMC) ')
print('=' * 50)

print('''O IMC é um parâmetro utilizado para avaliarse o peso está dentro 
do valor ideal para a altura. Isso significa que, a partir do resultado 
do IMC é possível saber se a pessoa está acima ou abaixo do peso recomendado 
e também diagnosticar problemas de saúde como obesidade ou desnutrição. 
Para saber seu IMC, informe o que pede:\n''')

x = float(input('Digite seu peso em (kg): '))
y = float(input('Digite sua altura em (m): '))

imc = x/y**2

print('O seu IMC é = {:.2f}.'.format(imc)) # {:.2f} >> PERMITE QUE SOMENTE DUAS CASAS DECIMAIS APAREÇÃO DEPOIS DA     VÍRGULA
                                           # .format() >> COLOCA O DADO DA VARIAVÉL DENTRO DAS {}
if imc < 18.5: # \033[36m \033[m >> COMANDOS PARA CORES NO TERMINAL
    print('''\n Você está abaixo do \033[36m Abaixo do peso ideal.\033[m 
Isso pode ser apenas uma característica pessoal, 
mas também pode ser um sinal de desnutrição ou de algum problema de saúde. 
Caso esteja perdendo peso sem motivo aparente, procure um médico.\n''')

elif 18.5 <= imc < 25: # OUTRA FORMA DE REPRESENTAR.
    print('''\n \033[32mParabéns!\033[m, você está com o \033[32mPeso normal! (Peso Ideal)\033[m 
Recomendamos que mantenha hábitos saudáveis em seu dia a dia. 
Especialistas sugerem ingerir de 4 a 5 porções diárias de frutas, 
verduras e legumes, além da prática de exercícios físicos, 
pelo menos 150 minutos semanais.\n''')

elif imc >= 25 and imc < 30:
    print('''\n \033[33mAtenção!\033[m Você está \033[33mAcima do peso ideal! (Sobrepeso)\033[m 
Alguns quilos a mais já são suficientes para que algumas pessoas desenvolvam 
doenças associadas, como diabetes e hipertensão. 
É importante rever seus hábitos. Procure um médico.\n''')

elif imc >= 30 and imc < 40:
    print('''\n \033[35mSinal de alerta!\033[m Você está na \033[35mObesidade!\033[m 
O excesso de peso é fator de risco para desenvolvimento de outros 
problemas de saúde. A boa notícia é que uma pequena perda de 
peso já traz benefícios à saúde. Procure um médico para 
definir o tratamento mais adequado para você.\n''')

else:
    print('''\n \033[31mSinal vermelho!\033[m Você está na \033[31mObesidade grave!\033[m 
Ao atingir este nível de IMC, o risco de doenças associadas está 
entre alto e muito alto. Busque ajuda de um profissional de saúde; 
não perca tempo.\n''')

print('Obs: Cálculos válidos apenas para adultos.\n')

dados = {
        'IMCs': '\033[36mMenor_que_18\033[m \033[32mEntre_18.5_e_24.9\033[m \033[33mEntre_25_e_29.9\033[m \033[35mEntre_30_e_39.9\033[m \033[31mAcima_de_40\033[m'.split(), # DIVIDE OS DADOS EM LISTAS
        'Classificação' : '\033[36mAbaixo_do_peso_ideal\033[m \033[32mPeso_normal\033[m \033[33mAcima_do_peso_ideal\033[m \033[35mObesidade\033[m \033[31mObesidade_grave\033[m'.split(),
        }

df_dados = pd.DataFrame(dados) # CRIA IM OBJETO DATAFRAME A PARTIR DE DIFERENTES TIPOS DE DADOS
                               
numero = 1
mensagem = '''Caso tenha alguma outra dúvida digite umas das opcões abaixo:
 0 - Finalizar o Atendimento 
 1 - Tabela do IMC\n '''

print(mensagem)

numero = int(input('Digite um número: '))
if numero == 0:
    print('Espero ter conseguido resolver a sua demanda da melhor forma possível. Tenha um ótimo dia!\n')
elif numero == 1:
    print(tabulate(df_dados, headers='keys', tablefmt='fancy_grid')) # ESPECIFICA O FORMATO DO CABEÇALHO E CORPO DA TABELA
elif numero != 0 or numero != 1:
    print('Espero ter conseguido resolver a sua demanda da melhor forma possível. Tenha um ótimo dia!\n')
