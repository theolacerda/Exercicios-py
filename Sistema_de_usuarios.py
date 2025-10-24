import json
import os

ARQUIVO_USUARIOS = "usuarios.json"

def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "r") as f:
            return json.load(f)
    else:
        return {
            'Lider': {'Lider': {'senha': '196292021tT'}},
            'Admin': {'Admin1': {'senha': '00009'}},
            'Cliente': {'Cliente1': {'senha': '99999', 'empresa': 'Logos'}},
            'Funcionario': {'Funcionario1': {'senha': '4241'}}
        }

def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w") as f:
        json.dump(usuarios, f, indent=4)

usuarios = carregar_usuarios()

pedidos_admin = []

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

        tentativas = 9
        while tentativas > 0:
            senha = input('Para entrar informe sua senha: ')
            if usuarios[tipo_usuario][usuario]['senha'] == senha:
                print(f'\nAcesso permitido! Bem-vindo, {usuario}.')
                voltar = 'operacoes'
                break
            else:
                tentativas -= 1
                if tentativas > 0:
                    print(f'Senha incorreta. Você tem mais {tentativas} tentativa(s).')
                    tentar = input('Deseja tentar novamente? ("sim" ou "não"): ').lower()
                    if tentar != 'sim':
                        print('Acesso cancelado.')
                        tentativas = 0
                        break
                else:
                    print('Número máximo de tentativas atingido. Acesso negado.')
                    voltar = 'sair'
                    break

        if tentativas == 0:
            continue

    if voltar == 'operacoes':

        if tipo_usuario == 'Lider':
            print(f'\nOlá {usuario}, seja bem-vindo ao sistema.')
            manutencao = input(
                '1 - Manutenção do sistema\n'
                '2 - Ver usuários\n'
                '3 - Ver funcionários\n'
                '4 - Cadastrar novos usuários\n'
                '5 - Analisar pedidos de novos Admins\n'
                '6 - Remover usuários do sistema\n'
                '7 - Sair do sistema\n'
                'Escolha uma opção: '
            )

            if manutencao == '1':
                print('Manutenção do sistema selecionada.')

            elif manutencao == '2':
                print('Lista completa de usuários:')
                for tipo, lista in usuarios.items():
                    print(f'\n{tipo}s:')
                    for nome, info in lista.items():
                        if tipo == 'Cliente':
                            empresa = info.get('empresa', 'N/A')
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
                    if novo_nome in usuarios[novo_tipo]:
                        print(f'Usuário "{novo_nome}" já existe! Escolha outro nome.')
                        continue
                    nova_senha = input(f'Informe a senha do novo {novo_tipo}: ')
                    if novo_tipo == 'Cliente':
                        empresa = input('Informe o nome da empresa do cliente: ')
                        usuarios[novo_tipo][novo_nome] = {'senha': nova_senha, 'empresa': empresa}
                        print(f'Cliente "{novo_nome}" cadastrado com sucesso (Empresa: {empresa}).')
                    else:
                        usuarios[novo_tipo][novo_nome] = {'senha': nova_senha}
                        print(f'{novo_tipo} "{novo_nome}" cadastrado com sucesso!')
                    salvar_usuarios(usuarios)

            elif manutencao == '5':
                if not pedidos_admin:
                    print('Nenhum pedido de novo administrador pendente.')
                else:
                    print('\nPedidos pendentes:')
                    for i, pedido in enumerate(pedidos_admin, 1):
                        print(f'{i}. Usuário: {pedido["nome"]}, Senha: {pedido["senha"]}')
                    escolha = input('Deseja aprovar algum pedido? (s/n): ').lower()
                    if escolha == 's':
                        indice = int(input('Informe o número do pedido para aprovar: ')) - 1
                        if 0 <= indice < len(pedidos_admin):
                            pedido = pedidos_admin.pop(indice)
                            usuarios['Admin'][pedido['nome']] = {'senha': pedido['senha']}
                            print(f'Novo administrador "{pedido["nome"]}" aprovado e cadastrado com sucesso!')
                            salvar_usuarios(usuarios)
                        else:
                            print('Número de pedido inválido.')

            elif manutencao == '6':
                print('Remover usuário do sistema:')
                tipo = input('Informe o tipo de usuário (Lider / Admin / Cliente / Funcionario): ').capitalize()
                if tipo in usuarios:
                    nome = input('Informe o nome do usuário a ser removido: ')
                    if nome in usuarios[tipo]:
                        del usuarios[tipo][nome]
                        print(f'Usuário "{nome}" removido com sucesso!')
                        salvar_usuarios(usuarios)
                    else:
                        print('Usuário não encontrado.')
                else:
                    print('Tipo inválido!')

            elif manutencao == '7':
                print('Saindo do sistema administrativo...')
                voltar = input('\nDeseja "trocar de usuario" ou "sair"?: ')
                continue

        elif tipo_usuario == 'Admin':
            print(f'\nOlá {usuario}, seja bem-vindo ao sistema.')
            manutencao = input(
                '1 - Manutenção do sistema\n'
                '2 - Ver usuários\n'
                '3 - Ver funcionários\n'
                '4 - Cadastrar novos usuários\n'
                '5 - Solicitar novo Admin\n'
                '6 - Sair do sistema\n'
                'Escolha uma opção: '
            )

            if manutencao == '1':
                print('Manutenção do sistema selecionada.')

            elif manutencao == '2':
                print('Lista completa de usuários:')
                for tipo, lista in usuarios.items():
                    print(f'\n{tipo}s:')
                    for nome, info in lista.items():
                        if tipo == 'Cliente':
                            empresa = info.get('empresa', 'N/A')
                            print(f'  - {nome} (Empresa: {empresa})')
                        else:
                            print(f'  - {nome}')

            elif manutencao == '3':
                print('Lista de funcionários:')
                print(", ".join(usuarios['Funcionario'].keys()))

            elif manutencao == '4':
                print('Cadastrar novo usuário:')
                novo_tipo = input('Informe o tipo de usuário (Cliente / Funcionario): ').capitalize()
                if novo_tipo not in usuarios:
                    print('Tipo inválido!')
                else:
                    novo_nome = input(f'Informe o nome do novo {novo_tipo}: ')
                    if novo_nome in usuarios[novo_tipo]:
                        print(f'Usuário "{novo_nome}" já existe! Escolha outro nome.')
                        continue
                    nova_senha = input(f'Informe a senha do novo {novo_tipo}: ')
                    if novo_tipo == 'Cliente':
                        empresa = input('Informe o nome da empresa do cliente: ')
                        usuarios[novo_tipo][novo_nome] = {'senha': nova_senha, 'empresa': empresa}
                        print(f'Cliente "{novo_nome}" cadastrado com sucesso (Empresa: {empresa}).')
                    else:
                        usuarios[novo_tipo][novo_nome] = {'senha': nova_senha}
                        print(f'{novo_tipo} "{novo_nome}" cadastrado com sucesso!')
                    salvar_usuarios(usuarios)

            elif manutencao == '5':
                print('\nSolicitar novo administrador:')
                novo_nome = input('Informe o nome do novo Admin: ')
                nova_senha = input('Informe a senha do novo Admin: ')
                pedidos_admin.append({'nome': novo_nome, 'senha': nova_senha})
                print(f'Pedido de criação do administrador "{novo_nome}" enviado para aprovação do Líder.')

            elif manutencao == '6':
                print('Saindo do sistema administrativo...')
                voltar = input('\nDeseja "trocar de usuario" ou "sair"?: ')
                continue

        elif tipo_usuario == 'Funcionario':
            print(f'\nOlá {usuario}, bem-vindo ao sistema de funcionários.')
            funcoes = input('1 - Ver tarefas\n2 - Ver agenda\n3 - Sair do sistema\nEscolha uma opção: ')
            if funcoes == '1':
                print('Suas tarefas: organizar relatórios, revisar planilhas e enviar status diário.')
            elif funcoes == '2':
                print('Agenda do dia: Reunião 10h, Almoço 12h, Relatórios 15h.')
            elif funcoes == '3':
                print('Saindo do sistema de funcionários...')
                voltar = input('\nDeseja "trocar de usuario" ou "sair"?: ')
                continue

        elif tipo_usuario == 'Cliente':
            empresa = usuarios['Cliente'][usuario]['empresa']
            print(f'\nOlá {usuario}, da empresa {empresa}! Seja bem-vindo.')
            ferramentas = input('1 - Acessar dados da empresa\n2 - Ver notícias\n3 - Sair do sistema\nEscolha uma opção: ')
            if ferramentas == '1':
                print(f'Aqui estão os dados da empresa {empresa}.')
            elif ferramentas == '2':
                print(f'Últimas notícias para clientes da empresa {empresa}.')
            elif ferramentas == '3':
                print('Saindo do sistema do cliente...')
                voltar = input('\nDeseja "trocar de usuario" ou "sair"?: ')
                continue

        voltar = input('\nDeseja "trocar de usuario", continuar as "operacoes" ou "sair"?: ')
        if voltar == 'sair':
            print('Sistema encerrado.')



