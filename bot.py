nome = input('Qual o seu nome? ')
print('Prazer em te conhecer,', nome, 'tudo bem? Eu sou um bot criado para ajudar você e juntar todos os sistemas feitos até agora!')

opcoes = input('O que você quer que eu faça hoje?'
               '\n1 - Conte uma piada'
               '\n2 - Acesse o sistema de Usuarios'
               '\n3 - Acesse a Calculadora'
               '\n4 - Sair '
               '\nDigite o número da opção desejada: ')

if opcoes == '1':
    print('Por que o livro de matemática se suicidou? Porque ele tinha muitos problemas!')

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
else:
    print('Opção inválida!')
