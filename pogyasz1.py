from Csomag import Csomag
def fajlbeolvasas():
    fajl = open("csomag.txt", "r", encoding = 'utf-8')
    fajl.readline()
    fajlbol_sorok_lista = fajl.readlines()
    print(fajlbol_sorok_lista)
    fajl.close()
    csomag_lista = []
    for i in range(0, len(fajlbol_sorok_lista), 1):
        akt_elem = fajlbol_sorok_lista[i]
        sor_lista = akt_elem.strip().split("#")
        a: int = int(sor_lista[0])
        b:int = int(sor_lista[1])
        c: int = int(sor_lista[2])
        m:int = int(sor_lista[3])
        csomag = Csomag(a, b, c, m)
        csomag_lista.append(csomag)
    
    return csomag_lista

def pogyasz_atlagsuly(lista):
    ossz: int = 0
    db: int = 0
    for i in range(0, len(lista), 1):
        if (lista[i].a == 51):
            ossz += lista[i].m
            db += 1
    
    print(ossz, db)
    return 1000*ossz/db

def legmagasabb(lista):
    max_ertek: int = 0
    max_index: int = 0
    for i in range(0, len(lista), 1):
        if (max_ertek < lista[i].b):
            max_ertek = lista[i].b
            max_index += 1
    
    
    return max_index