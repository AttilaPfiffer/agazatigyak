import pogyasz1

csomag_lista = pogyasz1.fajlbeolvasas()
print(f"\tA poggyászok száma: {len(csomag_lista)}")
print(f"Az első csomag szélessége: {csomag_lista[0].a}")

atlag: float = pogyasz1.pogyasz_atlagsuly(csomag_lista)
print(f"\tAz 51 cm-es poggyászok álag súlyértéke: {round(atlag)} g")

legmagasabb = pogyasz1.legmagasabb(csomag_lista)
print(f"\tA legmagasabb poggyász méretei: {csomag_lista[legmagasabb].a}")
