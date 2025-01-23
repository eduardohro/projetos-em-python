### FUNÇÕES PARA VOTAÇÃO ###

def voto(ano):
    """
    Determina a obrigatoriedade do voto com base no ano de nascimento.
    
    :param ano: Ano em que a pessoa nasceu.
    :return: String indicando se o voto é obrigatório, opcional ou não permitido.
    """
    from datetime import date
    idade = date.today().year - ano
    
    if idade < 16:
        situacao = 'NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        situacao = 'VOTO OPCIONAL'
    else: 
        situacao = 'VOTO OBRIGATÓRIO'
    
    return f'Com {idade} anos: {situacao}'

print('-=' * 20)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))


### FUNÇÕES PARA VOTAÇÃO, CURSO EM VIDEO ###

# def voto(ano):
#     from datetime import date
#     atual = date.today().year
#     idade = atual - ano
#     if idade < 16:
#         return f'Com {idade} anos: NÃO VOTA.'
#     elif 16 <= idade < 18 or idade > 65:
#         return f'Com {idade} anos: VOTO OPCIONAL.'
#     else:
#         return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    
# # Programa Principal
# nasc = int(input('Em que ano você nasceu? '))
# print(voto(nasc))