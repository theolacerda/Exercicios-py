usuarios_registrados = []

voltar = 'trocar de usuario'  # Começa pedindo login

while voltar != 'sair':
    if voltar == 'trocar de usuario':
        usuario = input('Informe seu nome de usuário: ')

        if usuario not in ['Admin', 'Visitante', 'Funcionario']:
            print('Usuário não cadastrado. Acesso negado.')
            print('Sistema encerrado.')
            break
        else:
            print('Olá', usuario, 'seja bem-vindo ao sistema de acesso!')
            senha = input('Para entrar informe sua senha: ')

            while senha not in ['196292021tT', '99999', '4241']:
                print('Acesso negado.')
                senha = input('Senha incorreta. Tente novamente: ')

            usuarios_registrados.append(usuario)
            print(f"Usuário '{usuario}' registrado com sucesso.\n")

    # A partir daqui o usuário já está logado
    if usuario == 'Admin' and senha == '196292021tT':
        print('Acesso permitido.')
        print('Bem-vindo Administrador.')
        manutenção = input('1- Manutenção do sistema 2- Ver usuários 3- Ver funcionários 4- Sair do sistema: ')
        if manutenção == '1':
            print('Manutenção do sistema selecionada.')
        elif manutenção == '2':
            print('Lista de usuários registrados:', usuarios_registrados)
        elif manutenção == '3':
            print('Lista de funcionários: Funcionario1, Funcionario2, Funcionario3')
        elif manutenção == '4':
            print('Saindo do sistema.')

    elif usuario == 'Funcionario' and senha == '4241':
        print('Acesso permitido.')
        print('Bem-vindo Funcionário.')
        funcoes = input('1- Ver tarefas 2- Ver agenda 3- Sair do sistema: ')

    elif usuario == 'Visitante' and senha == '99999':
        print('Acesso permitido.')
        print('Bem-vindo Usuário.')
        ferramentas = input('1- Acessar dados da sua empresa 2- Ver notícias 3- Sair do sistema: ')

    voltar = input('\nDeseja "trocar de usuario", continuar as "operações" ou "sair"?: ')
    if voltar == 'sair':
        print('Sistema encerrado.')




