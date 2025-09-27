sai = float(input('Digite 1 para usar a calculadora e 0 para sair: '))

while (sai == 1):
    num1 = float(input('Digite o primeiro numero: '))
    num2 = float(input('Digite o segundo numero: '))
    ope = input('Digite a operação desejada (+, -, *, /): ')

    match ope:
        case "+":
            print('O resultado da soma é igual a:', num1 + num2)

        case "-":
            print('O resultado da subtração é igual a:', num1 - num2)

        case "*":
            print('O resultado da multiplicação é igual a:', num1 * num2)

        case "/":
            print('O resultado da divisão é igual a:', num1 / num2)

    
    sai = float(input('Digite 1 para fazer outro cálculo e 0 para sair: '))

    if sai != 1:
        print('Saindo da calculadora.')
        break
