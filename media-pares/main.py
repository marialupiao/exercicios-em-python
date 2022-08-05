n: int
soma: int
pares: int
media: float

n = int(input("Quantos elementos terao no vetor? "))

vet = [0 for x in range(n)]

for i in range(n):
    vet[i] = int(input("Digite um numero: "))

pares = 0
soma = 0

for i in range(n):
    if vet[i] % 2 == 0:
        soma = soma + vet[i]
        pares = pares + 1

if pares == 0:
    print("NENHUM NUMERO PAR")
else:
    media = float(soma) / pares

    print(f"MEDIA DOS PARES = {media:.1f}")