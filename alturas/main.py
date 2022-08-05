n: int
nMenores: int
total: float
media: float
percent: float

n = int(input("Quantas pessoas serao digitadas? "))

nomes = [0 for x in range(n)]
idades = [0 for x in range(n)]
alturas = [0 for x in range(n)]

for i in range(n):
    print(f"Dados da {i+1}a pessoa: ")
    nomes[i] = str(input("Nome: "))
    idades[i] = int(input("Idade: "))
    alturas[i] = float(input("Altura: "))

nMenores = 0
total = 0

for i in range(n):
    if idades[i] < 16:
        nMenores = nMenores + 1
        total = total + alturas[i]

media = total / nMenores
percent = (float(nMenores) / n) * 100.0

print()
print(f"Altura media = {media:.2f}")
print(f"Pessoas com menos de 16 anos: {percent:.1f}%")

for i in range(n):
    if idades[i] < 16:
        print(nomes[i])
