n: int
ratos: int
sapos: int
coelhos: int
qtdCobaias: int
total: int
tipo: str
pRatos: float
pSapos: float
pCoelhos: float

n = int(input("Quantos casos de teste serao digitados? "))

ratos = 0
sapos = 0
coelhos = 0

for i in range(n):
    qtdCobaias = int(input("Quantidade de cobaias: "))
    tipo = str(input("Tipo de cobaia: "))

    if tipo == 'R':
        ratos = ratos + qtdCobaias
    elif tipo == 'S':
        sapos = sapos + qtdCobaias
    else:
        coelhos = coelhos + qtdCobaias

total = ratos + sapos + coelhos
pCoelhos = (float(coelhos) / total) * 100.0
pSapos = (float(sapos) / total) * 100.0
pRatos = (float(ratos) / total) * 100.0

print()
print("RELATORIO FINAL: ")
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {pCoelhos:.2f}")
print(f"Percentual de ratos: {pRatos:.2f}")
print(f"Percentual de sapos: {pSapos:.2f}")

