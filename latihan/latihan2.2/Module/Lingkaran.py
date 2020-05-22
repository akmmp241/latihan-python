from Tool import clc,jeda

def lingkaran():
    clc.clc()

    print("\t\t\tLingkaran")

    jari = int(input("\nMasukan nilai jari: "))

    if (jari % 7) == 0:
        luas = (22/7) * jari**2
    else:
        luas = 3.14 * jari**2

    print("\nLusanya adalah ", luas)