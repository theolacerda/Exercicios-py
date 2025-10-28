nome = input('Qual o seu nome? ')
print('Prazer em te conhecer', nome, 'Tudo bem? Eu sou um bot criado para ajudar você e juntar todos os sistemas feitos até agora!')
voltar = 'sim'
while voltar == 'sim':

    opcoes = input('O que você quer que eu faça hoje?'
                   '\n1 - Conte uma piada'
                   '\n2 - Acesse o sistema de Usuarios'
                   '\n3 - Acesse a Calculadora'
                   '\n4 - Sair '
                   '\nDigite o número da opção desejada: ')

    if opcoes == '1':
        piadas = 'sim'
        while piadas == 'sim':
         import importlib
         import piadas
         importlib.reload(piadas)
         piadas = input('Quer ouvir outra piada? ("sim" ou "não") ')
        

    elif opcoes == '2':
        import importlib
        import Sistema_de_usuarios
        importlib.reload(Sistema_de_usuarios)

    elif opcoes == '3':
        import importlib
        import Calculadora
        importlib.reload(Calculadora)

    elif opcoes == '4':
        print('Obrigado por usar o bot! Até mais!')
        break
    else:
        print('Opção inválida!')
