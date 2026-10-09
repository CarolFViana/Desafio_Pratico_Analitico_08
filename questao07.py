# 7. Uma empresa de construção precisa calcular rapidamente a área de diferentes
# figuras geométricas. Crie três funções para a área do triângulo, área do trapézio e
# área do losango.

def area_triangulo(base, altura):
    return (base * altura) / 2


def area_trapezio(base_maior, base_menor, altura):
    return ((base_maior + base_menor) * altura) / 2


def area_losango(diagonal_maior, diagonal_menor):
    return (diagonal_maior * diagonal_menor) / 2


base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))

print(f"Área do triângulo: {area_triangulo(base, altura):.2f}")

base_maior = float(input("Digite a base maior do trapézio: "))
base_menor = float(input("Digite a base menor do trapézio: "))
altura_trapezio = float(input("Digite a altura do trapézio: "))

print(
    f"Área do trapézio: "
    f"{area_trapezio(base_maior, base_menor, altura_trapezio):.2f}"
)

diagonal_maior = float(input("Digite a diagonal maior do losango: "))
diagonal_menor = float(input("Digite a diagonal menor do losango: "))

print(
    f"Área do losango: "
    f"{area_losango(diagonal_maior, diagonal_menor):.2f}"
)