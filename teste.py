import json

with open("teste.json", "r") as arquivo:
    dados = json.load(arquivo)

print(dados)

dados["sexo"].append("masculiu")

with open("teste.json", "r") as arquivo:
    json.dump(dados, arquivo, indent=4)

print(dados)
