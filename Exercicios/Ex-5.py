
usuarios = {
    'Admin': {'Admin1': {'senha': '196292021tT'}},
    'Cliente': {'Cliente1': {'senha': '99999', 'empresa': 'Maped'}},
    'Funcionario': {'Funcionario1': {'senha': '4241'}}
    
}

voltar = 'trocar de usuario'

while voltar != 'sair':
    if voltar == 'trocar de usuario':
        usuario = input('Informe seu nome de usuário: ')

        
        tipo_usuario = None
        for tipo, lista in usuarios.items():
            if usuario in lista:
                tipo_usuario = tipo
                break

        if not tipo_usuario:
            print('Usuário não cadastrado. Acesso negado.')
            print('Sistema encerrado.')
            break

        senha = input('Para entrar informe sua senha: ')
        if usuarios[tipo_usuario][usuario]['senha'] != senha:
            print('Senha incorreta. Acesso negado.')
            break

       
        if tipo_usuario == 'Admin':
            print(f'Olá {usuario}, seja bem-vindo ao sistema')
            manutencao = input(
                '1- Manutenção do sistema\n''2- Ver usuários\n''3- Ver funcionários\n''4- Cadastrar novos usuários\n''5- Sair do sistema\n'
            )

            if manutencao == '1':
                print('Manutenção do sistema selecionada.')

            elif manutencao == '2':
                print('Lista completa de usuários:')
                for tipo, lista in usuarios.items():
                    print(f'{tipo}s:')
                    for nome in lista.keys():
                        if tipo == 'Cliente':
                            empresa = lista[nome].get('empresa', 'N/A')
                            print(f'  - {nome} (Empresa: {empresa})')
                        else:
                            print(f'  - {nome}')

            elif manutencao == '3':
                print('Lista de funcionários:')
                print(", ".join(usuarios['Funcionario'].keys()))

            elif manutencao == '4':
                print('Cadastrar novo usuário:')
                novo_tipo = input('Informe o tipo de usuário (Admin / Cliente / Funcionario): ').capitalize()
                if novo_tipo not in usuarios:
                    print('Tipo inválido!')
                else:
                    novo_nome = input(f'Informe o nome do novo {novo_tipo}: ')
                    nova_senha = input(f'Informe a senha do novo {novo_tipo}: ')
                    
                    if novo_tipo == 'Cliente':
                        empresa = input('Informe o nome da empresa do cliente: ')
                        usuarios[novo_tipo][novo_nome] = {'senha': nova_senha, 'empresa': empresa}
                        print(f'Cliente "{novo_nome}" cadastrado com sucesso (Empresa: {empresa}).')
                    else:
                        usuarios[novo_tipo][novo_nome] = {'senha': nova_senha}
                        print(f'{novo_tipo} "{novo_nome}" cadastrado com sucesso!')

            elif manutencao == '5':
                print('Saindo do sistema administrativo...')

        
        elif tipo_usuario == 'Funcionario':
            print(f'Olá {usuario}, bem-vindo ao sistema')
            funcoes = input('1- Ver tarefas\n2- Ver agenda\n3- Sair do sistema\nEscolha uma opção: ')
            if funcoes == '1':
                print('Suas tarefas: organizar relatórios, revisar planilhas e enviar status diário.')
            elif funcoes == '2':
                print('Agenda do dia: Reunião 10h, Almoço 12h, Relatórios 15h.')

       
        elif tipo_usuario == 'Cliente':
            empresa = usuarios['Cliente'][usuario]['empresa']
            print(f'Olá {usuario}, da empresa {empresa}! Seja bem-vindo.')
            ferramentas = input('1- Acessar dados da empresa\n2- Ver notícias\n3- Sair do sistema\nEscolha uma opção: ')
            if ferramentas == '1':
                print(f'Aqui estão os dados da empresa {empresa}.')
            elif ferramentas == '2':
                print(f'Últimas notícias para clientes da empresa {empresa}.')

    voltar = input('\nDeseja "trocar de usuario", continuar as "operações" ou "sair"?: ')
    if voltar == 'sair':
        print('Sistema encerrado.')


