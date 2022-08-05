n: int
maior: int

n = int(input("Qual a ordem da matriz? "))

mat = [[0 for x in range(n)]for x in range(n)]
maiorlinha: int = []

for i in range(n):
    for j in range(n):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

for i in range(n):
    maior = mat[i][0]
    for j in range(n):
        if maior < mat[i][j]:
            maior = mat[i][j]

    maiorlinha.append(maior)

print("MAIOR ELEMENTO DE CADA LINHA: ")
for i in range(n):
    print(maiorlinha[i])
