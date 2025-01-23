tempo_h = int(input())
media_velo = int(input())

distancia = tempo_h * media_velo

litros_por_km = distancia / 12

print(f"{litros_por_km:.3f}")
