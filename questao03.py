# 3. Uma escola deseja armazenar as notas de seus alunos utilizando uma lista dentro
# de outra lista. Cada lista interna representa um aluno e contém suas três notas
# obtidas durante o semestre.
# Considere a seguinte estrutura:

# alunos = [
# ["Ana", 7.5, 8.0, 9.0],
# ["Bruno", 6.0, 5.5, 7.0],
# ["Carlos", 9.0, 8.5, 10.0],
# ["Daniela", 5.0, 6.0, 4.5],
# ["Eduardo", 8.0, 7.5, 6.5]
# ]

# Cada elemento da lista alunos possui a seguinte estrutura:

# [nome, nota1, nota2, nota3]

# Sua tarefa é criar um programa em Python que percorra essa lista e apresente um
# relatório contendo:
# a) O nome de cada aluno;
# b) A média das três notas de cada aluno;
# c) Se o aluno está aprovado ou reprovado, considerando que a média mínima
# para aprovação é 7,0;
# d) a média geral da turma;
# e) o nome do aluno com a maior média;
# f) o nome do aluno com a menor média;
# g) quantos alunos foram aprovados;
# h) quantos alunos foram reprovados.

alunos = [
    ["Ana", 7.5, 8.0, 9.0],
    ["Bruno", 6.0, 5.5, 7.0],
    ["Carlos", 9.0, 8.5, 10.0],
    ["Daniela", 5.0, 6.0, 4.5],
    ["Eduardo", 8.0, 7.5, 6.5]
]

soma_medias = 0
aprovados = 0
reprovados = 0

maior_media = 0
menor_media = 10

aluno_maior_media = ""
aluno_menor_media = ""

for aluno in alunos:
    nome = aluno[0]

    media = (aluno[1] + aluno[2] + aluno[3]) / 3

    soma_medias += media

    if media >= 7:
        situacao = "Aprovado"
        aprovados += 1
    else:
        situacao = "Reprovado"
        reprovados += 1

    if media > maior_media:
        maior_media = media
        aluno_maior_media = nome

    if media < menor_media:
        menor_media = media
        aluno_menor_media = nome

    print(f"Aluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
    print()

media_geral = soma_medias / len(alunos)

print(f"Média geral da turma: {media_geral:.2f}")
print(f"Aluno com maior média: {aluno_maior_media}")
print(f"Aluno com menor média: {aluno_menor_media}")
print(f"Quantidade de aprovados: {aprovados}")
print(f"Quantidade de reprovados: {reprovados}")