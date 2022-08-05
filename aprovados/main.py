n: int
media: float

n = int(input("Quantos alunos serao digitados? "))

nome = [0 for x in range(n)]
nota1 = [0 for x in range(n)]
nota2 = [0 for x in range(n)]

for i in range(n):
    print(f"Digite nome, primeira e segunda nota do {i+1}o aluno: ")
    nome[i] = str(input())
    nota1[i] = float(input())
    nota2[i] = float(input())

print("Alunos aprovados:")

for i in range(n):
    media = (nota1[i] + nota2[i]) / 2

    if media >= 6.0:
        print(nome[i])