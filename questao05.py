# 5. Um estacionamento cobra seus clientes de acordo com o tempo que o veículo
# permaneceu no local:
# Tempo de permanência Valor
# Até 1 hora R$ 5,00
# De 1 a 3 horas R$ 10,00
# De 3 a 5 horas R$ 15,00
# Mais de 5 horas R$ 20,00

# Crie um código (principal) que receba as informações relevantes para a situação.
# Crie uma função para o cálculo do valor final do estacioamento.

def calcular_estacionamento(horas):
    if horas <= 1:
        return 5.00
    elif horas <= 3:
        return 10.00
    elif horas <= 5:
        return 15.00
    else:
        return 20.00


tempo = float(input("Digite o tempo de permanência em horas: "))

valor = calcular_estacionamento(tempo)

print(f"Valor do estacionamento: R$ {valor:.2f}")