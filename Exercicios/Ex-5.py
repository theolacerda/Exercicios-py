usuario = input('Informe seu nome de usuário:')

if (usuario != 'Admin' and usuario != 'Visitante' and usuario != 'Funcionario'): 
    print('Usuário não cadastrado. Acesso negado.')
    print('Sistema encerrado')
if (usuario == 'Admin' or usuario == 'Visitante' or usuario == 'Funcionario'):
    print('Olá', usuario, 'seja bem vindo ao sistema de acesso!')
    senha = input('Para entrar informe sua senha:')

while (senha != '196292021tT' and senha != '99999' and senha != '4241'):
    print('Acesso negado')
    senha = input('Senha incorreta. Tente novamente:')

if (usuario == 'Admin' and senha == '196292021tT'):
    print('Acesso permitido')
    print('Bem vindo Administrador')
    print('O que deseja fazer em nosso sistema?')
    manutenção = input('1- Manutenção do sistema 2- Ver usuários 3- Ver funcionarios 4- Sair do sistema: ')

elif (usuario == 'Funcionario' and senha == '4241'):
    print('Acesso permitido')
    print('Bem vindo Funcionário')
    print('O que deseja verificar?')
    funçoes = input('1- Ver tarefas 2- Ver agenda 3- Sair do sistema:')

elif (usuario == 'Visitante' and senha == '99999'):
    print('Acesso permitido') 
    print('Bem vindo Usuário')
    print('Que ferramenta Deseja usar?')
    ferramentas = input ('1- Acessar dados da sua empresa 2- Ver notícias 3- Sair do sistema: ')



