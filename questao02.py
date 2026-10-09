# 2. Uma caixa contém:
# bolas = ["vermelha", "azul", "verde", "vermelha", "amarela", "azul", “vermelha",
# "verde", "azul", "vermelha"]
# Considerando que uma bola será escolhida ao acaso, crie um programa que:
# a) conte quantas bolas existem na caixa;
# b) conte quantas são vermelhas;
# c) calcule a probabilidade de escolher uma bola vermelha;
# d) apresente a probabilidade em forma de fração e porcentagem.

bolas = [
    "vermelha", "azul", "verde", "vermelha", "amarela",
    "azul", "vermelha", "verde", "azul", "vermelha"
]

total_bolas = len(bolas)

bolas_vermelhas = bolas.count("vermelha")

probabilidade = bolas_vermelhas / total_bolas

porcentagem = probabilidade * 100

print(f"Total de bolas: {total_bolas}")
print(f"Quantidade de bolas vermelhas: {bolas_vermelhas}")
print(f"Probabilidade em fração: {bolas_vermelhas}/{total_bolas}")
print(f"Probabilidade em porcentagem: {porcentagem:.0f}%")