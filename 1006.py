nota_a = float(input())
nota_b = float(input())
nota_c = float(input())

if (
    (nota_a < 0 or nota_a > 10)
    or (nota_b < 0 or nota_b > 10)
    or (nota_c < 0 or nota_c > 10)
):
    print("Nota invalida")
else:
    media = ((nota_a * 2) + (nota_b * 3) + (nota_c * 5)) / 10
    print(f"MEDIA = {media:.1f}")
