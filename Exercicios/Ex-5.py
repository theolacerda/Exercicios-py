senha = input('Para entrar informe sua senha:')

while (senha != '196292021tT' and senha != '99999'):
        print('Acesso negado')
        senha = input('Senha incorreta. Tente novamente:')

if (senha == '196292021tT'):
        print('Acesso permitido')
        print('Bem vindo Administrador')
        print('O que deseja fazer em nosso sistema?')
    
elif (senha == '99999'):
        print('Acesso permitido')
        print('Bem vindo Usuário')
        print('O que deseja fazer em nosso sistema?')

else:
    print('Sistema encerrado')
