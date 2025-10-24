nome = input('Qual o seu nome? ')
print('Prazer em te conhecer', nome, '! Tudo bem? Eu sou um bot criado para ajudar você e juntar todos os sistemas feitos até agora!')
ult = input('Quando você quiser sair, é só digitar "sair", caso contrario digite "continuar" ')
if ult == 'sair':
    print('Tudo bem, até mais!')
    exit()
while ult == 'continuar':

 opcoes = input('O que você quer que eu faça hoje?'
               '\n1 - Conte uma piada'
               '\n2 - Acesse o sistema de Usuarios'
               '\n3 - Acesse a Calculadora'
               '\n4 - Sair '
               '\nDigite o número da opção desejada: ')

 if opcoes == '1':
    saida = input(' Voce quer ouvir uma piada? se "sim" continue, quando nao quiser mais digite não: "').lower()
    if saida != 'sim':
        print('Tudo bem, até mais!')
    while saida != 'não':
         import importlib
         import piadas
         importlib.reload(piadas)
         saida = input(' Voce quer ouvir mais uma piada? se "sim" continue, quando nao quiser mais digite não"').lower()
    

 elif opcoes == '2':
    saida = input(' Voce quer entrar no sistema de usuarios? se "sim" continue, quando nao quiser mais digite não: "').lower()
    if saida != 'sim':
        print('Tudo bem, até mais!')
    while saida != 'não':
     import importlib
     import Sistema_de_usuarios
     importlib.reload(Sistema_de_usuarios)
    saida = input(' Voce quer continuar no sistema de usuarios? se "sim" continue, quando nao quiser mais digite não"').lower()

 elif opcoes == '3':
    saida = input(' Voce quer entrar na calculadora? se "sim" continue, quando nao quiser mais digite não: "').lower()
    if saida != 'sim':
        print('Tudo bem, até mais!')
    while saida != 'não':
     import importlib
     import Calculadora
     importlib.reload(Calculadora)
    saida = input(' Voce quer continuar os calculos? se "sim" continue, quando nao quiser mais digite não"').lower()

 elif opcoes == '4':
    print('Obrigado por usar o bot! Até mais!')
 else:
    print('Opção inválida!')
