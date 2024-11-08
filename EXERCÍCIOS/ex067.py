### TABUADA V3.0 ###

while True:
    print('—'*40)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('—'*40)

    tabuada = 1

    if num < 0:
        break

    while tabuada <= 10:
        print(f'{num} x {tabuada} = {num * tabuada}')
        tabuada += 1
        
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!\n')