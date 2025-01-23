### ANALISANDO E GERANDO DICIONÁRIOS ###

def notas(*n, sit=False):
    """
    -> Analisa notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita múltiplos valores).
    :param sit: (opcional) Indica se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre as notas.
    """
    resp = dict()
    resp['total'] = len(n)
    resp['maior'] = max(n)
    resp['menor'] = min(n)
    resp['média'] = sum(n) / len(n)

    if sit:
        if resp['média'] >= 7:
            resp['situação'] = 'PM - Progrediu Muito!'
        elif 5 <= resp['média'] < 7:
            resp['situação'] = 'PR - Progrediu Regularmente!'
        else:
            resp['situação'] = 'PP - Progrediu Pouco!'

    return resp

resp = notas(3.5, 2, 10, 6.5, 8, 9, 10, sit=True)
print(resp)
