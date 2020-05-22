from Tool.clearScreen import clearScreen as clc
from Tool.isLanjutkan import isLanjutkan as lanjut


def persegi():
    start = True

    while start:
        clc()
        print("Persegi\n")

        sisi = int(input("Masukan nilai sisi: "))

        luas = sisi * sisi

        print("\nLuasnya adalah ", luas)

        lanjut(start, 5)