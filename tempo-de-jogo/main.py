hInicial: int
hFinal: int
resp: int

hInicial = int(input("Hora inicial: "))
hFinal = int(input("Hora final: "))

if hInicial < hFinal:
    resp = hFinal - hInicial
else:
    resp = 24 - (hInicial - hFinal)

print(f"O JOGO DUROU {resp} HORA(S)")