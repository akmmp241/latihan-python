from Tool import clc

def segitiga():
    clc.clc()

    print("\t\t\tSegitiga\n")

    alas = int(input("Masukan nilai alas: "))
    tinggi = int(input("\nMasukan nilai tinggi: "))

    luasAsli = (1/2) * alas * tinggi

    if luasAsli % 2 == 0:
        luas = int(luasAsli)
        print("\nLuasnya adalah ", luas)
    else:
        print("\nLuasnya adalah ", luasAsli)

    
