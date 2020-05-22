from Tool.clearScreen import clearScreen as clc
from Module import Persegi

def Hitungluas():
    clc()
    print("Ketikan 'keluar' jika ingin keluar")
    input("")

    start = True

    while start:
        clc()
        print("HitungLuas\n")
        print("1.Persegi")
        print("2.persegi panjang")
        print("0.keluar")

        menu = input("\nMasukan pilihan: ")

        if menu == "1":
            Persegi.persegi()
        elif menu == "2":
            print("persegi panjang")
            input("")
        elif menu == "0":
            exit()
        else:
            print("menu tidak ditemukan")
            input("")

        clc()

Hitungluas()