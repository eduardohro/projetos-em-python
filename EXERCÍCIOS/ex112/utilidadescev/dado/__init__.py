def leiaDinheiro(msg):
    while True:
        n = input(msg).strip().replace(',', '.')
        try:
            return float(n)
        except ValueError:
            print(f'\033[31mERRO! "{n}" é um preço inválido!\033[m')


### CURSO EM VIDEO ###

# def leiaDinheiro(msg):
#     válido = False
#     while not válido:
#         entrada = str(input(msg)).replace(',', '.').strip()
#         if entrada.isalpha() or entrada == '':
#             print(f'\033[31mERRO: \"{entrada}\" é um preço enválido!\033[m')
#         else:
#             válido = True
#             return float(entrada)