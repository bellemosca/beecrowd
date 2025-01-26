tempo = int(input())

seg = tempo % (24 * 3600)
horas = tempo // 3600
seg = seg % 3600
min = seg // 60
seg %= 60

print(f"{horas}:{min}:{seg}")
