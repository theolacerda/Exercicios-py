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

pedidos_cliente = []
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
            resp = input('Usuário não cadastrado. Deseja cadastrar? ("sim" ou "não"): ').lower()
            if resp == 'sim':
                resp_cliente = input('Você é um cliente interessado em entrar no nosso sistema? ("sim" ou "não"): ').lower()
                
                if resp_cliente == 'sim':
                    print('\nSolicitar novo Cliente:')
                    novo_nome = input('Informe seu nome Cliente: ')
                    nova_senha = input('Informe a senha desejada: ')
                    pedidos_cliente.append({'nome': novo_nome, 'senha': nova_senha})
                    print(f'Pedido de criação de cliente "{novo_nome}" enviado para aprovação do Líder.')
                else:
                    print('Por favor, entre em contato com o administrador do sistema para criar uma conta.')

            else:
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
                '5 - Analisar pedidos de novos Colaboradores\n'
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
                if not pedidos_cliente:
                    print('Nenhum pedido de novo cliente pendente.')
                else:
                    print('\nPedidos de novos clientes:')
                    for i, pedido in enumerate(pedidos_cliente, 1):
                        print(f'{i}. Nome: {pedido["nome"]}, Senha: {pedido["senha"]}')
                    escolha = input('Deseja aprovar algum pedido de cliente? (s/n): ').lower()
                    if escolha == 's':
                        indice = int(input('Informe o número do pedido para aprovar: ')) - 1
                        if 0 <= indice < len(pedidos_cliente):
                            pedido = pedidos_cliente.pop(indice)
                            empresa = input(f'Informe a empresa do cliente "{pedido["nome"]}": ')
                            usuarios['Cliente'][pedido['nome']] = {'senha': pedido['senha'], 'empresa': empresa}
                            print(f'Cliente "{pedido["nome"]}" aprovado e cadastrado com sucesso!')
                            salvar_usuarios(usuarios)
                        else:
                            print('Número de pedido inválido.')

                if not pedidos_admin:
                    print('Nenhum pedido de novo administrador pendente.')
                else:
                    print('\nPedidos de novos administradores:')
                    for i, pedido in enumerate(pedidos_admin, 1):
                        print(f'{i}. Usuário: {pedido["nome"]}, Senha: {pedido["senha"]}')
                    escolha = input('Deseja aprovar algum pedido de admin? (s/n): ').lower()
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

        voltar = input('\nDeseja "trocar de usuario", continuar as "operacoes" ou "sair"?: ')
        if voltar == 'sair':
            print('Sistema encerrado.')