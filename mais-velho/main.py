n: int
maior: int
posicao: int

n = int(input("Quantas pessoas voce vai digitar? "))

nomes = [0 for x in range(n)]
idades = [0 for x in range(n)]

for i in range(n):
    print(f"Dados da {i+1}a pessoa: ")
    nomes[i] = str(input("Nome: "))
    idades[i] = int(input("Idade: "))

maior = idades[0]
posicao = 0

for i in range(n):
    if idades[i] > maior:
        maior = idades[i]
        posicao = i

print(f"PESSOA MAIS VELHA: {nomes[posicao]}")