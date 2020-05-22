from Tool import clc,jeda

def lingkaran():
    clc.clc()

    print("Lingkaran")

    jari = int(input("Masukan nilai jari: "))

    if (jari % 7) == 0:
        luas = (22/7) * jari**2
    else:
        luas = 3.14 * jari**2

    print("Lusanya adalah ", luas)