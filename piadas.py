import json
import random
import os

ARQUIVO_HISTORICO = "historico.json"
MAX_HISTORICO = 7

if os.path.exists(ARQUIVO_HISTORICO):
    with open(ARQUIVO_HISTORICO, "r") as f:
        historico = json.load(f)
else:
    historico = []


piadas = [
    "Por que o livro de matemática se suicidou? Porque tinha muitos problemas!",
    "O que o zero disse para o oito? Belo cinto!",
    "Por que o computador foi ao médico? Porque pegou um vírus!",
    "Qual é o cúmulo da paciência? Esperar o café esfriar!",
    "Por que o jacaré tirou o jacarezinho da escola? Porque ele réptil de ano!",
    "O que o tomate foi fazer no banco? Tirar extrato!",
    "Por que a vaca foi para o espaço? Para se encontrar com a Via Láctea!"
]

piadas_disponiveis = [p for p in piadas if p not in historico]

if not piadas_disponiveis:
    historico = []
    piadas_disponiveis = piadas.copy()
piada_escolhida = random.choice(piadas_disponiveis)
print(piada_escolhida)
historico.append(piada_escolhida)
if len(historico) > MAX_HISTORICO:
    historico.pop(0)
with open(ARQUIVO_HISTORICO, "w") as f:
    json.dump(historico, f)
    