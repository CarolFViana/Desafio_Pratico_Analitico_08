# 1. Faça um programa em Python que receba 10 idades, calcule e exiba:
# a) a média das idades;
# b) a mediana;
# c) a moda.

idades = []

for i in range(10):
    idade = int(input("Digite uma idade: "))
    idades.append(idade)

# Média
media = sum(idades) / len(idades)

# Mediana
idades.sort()
mediana = (idades[4] + idades[5]) / 2

# Moda
moda = max(idades, key=idades.count)

print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")