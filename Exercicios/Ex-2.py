print('Você deseja um laço infinito ou com parada?')
ope = input("Digite 'parada' ou 'infinito': ")

if ope == 'parada':
    for c in range(1, 11):
        print(c)

elif ope == 'infinito':
    num = 0 
    while True:
        num += 1
        print(num)
