nota_a = float(input())
nota_b = float(input())

if nota_a < 0 or nota_a > 10:
    print("Nota A inválida")
    exit()
if nota_b < 0 or nota_b > 10:
    print("Nota B inválida")
    exit()
else:
    media = ((nota_a * 3.5) + (nota_b * 7.5)) / 11
    print(f"MEDIA = {media:.5f}")
