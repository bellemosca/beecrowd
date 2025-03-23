A, B, C = map(int, input().split())

valores = [A, B, C]
ordem_cres = sorted(valores)

for num in ordem_cres:
    print(num)
print()
for valor in valores:
    print(valor)
