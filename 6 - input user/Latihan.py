import os


def HitungLuas():
    clearScreen()

    print("\n\t\t\t\tHitungLuas\t\t\t\n")
    print("1.Persegi")
    print("2.Persegi panjang")
    print("3.Segitiga")
    print("4.Lingkaran")
    print("0.Keluar")

    user = input("\nPilihan anda: ")

    if user == "1":
        persegi()
    elif user == "2":
        persegiPanjang()
    elif user == "3":
        segitiga()
    elif user == "4":
        lingkaran()
    elif user == "0":
        print("BYE!")
        exit()
    else:
        print("pilihan tidak di temukan")
        display()


def display():
    # menjeda program
    input("")
    HitungLuas()


def clearScreen():
    os.system("clear")


def persegi():
    clearScreen()

    print("\n\t\t\t\tPersegi\t\t\t\n")

    sisi = int(input("masukan panjang sisi: "))

    luas = sisi * sisi

    print("\nLuasnya adalah ", luas)

    isLanjutkan()


def persegiPanjang():
    clearScreen()

    print("\n\t\t\t\tPersegi Panjang\t\t\t\n")

    panjang = int(input("Masukan nilai panjang: "))
    lebar = int(input("\nMasukan nilai lebar: "))

    luas = panjang * lebar

    print("\nLuasnya adalah ", luas)

    isLanjutkan()


def segitiga():
    clearScreen()

    print("\n\t\t\t\tSegitiga\t\t\t\n")

    alas = int(input("Masukan nilai alas: "))
    tinggi = int(input("\nMasukan nilai tinggi: "))

    luas = 0.5 * (alas * tinggi)

    # luas = int(luas)

    print("\nLuasnya adalah ", luas)

    isLanjutkan()


def lingkaran():
    clearScreen()

    tujuh = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

    print("\n\t\t\t\tLingkaran\t\t\t\n")

    jari = int(input("Masukan nilai jari: "))

    if jari in tujuh:
        luasAsli = (22/7) * jari**2
        luas = int(luasAsli)
    else:
        luasAsli = 3.14 * jari**2
        luas = int(luasAsli + 1)

    print("\nLuasnya adalah ", luas)

    isLanjutkan()


def isLanjutkan():
    isLanjutkan = input("\n\nApakah anda ingin melanjutkan? (y/n) ")

    if isLanjutkan == "y":
        display()
    elif isLanjutkan == "n":
        print("BYE!")
        exit()

    while isLanjutkan not in ("y", "n"):
        isLanjutkan = input("\n\nApakah anda ingin melanjutkan? (y/n) ")

        if isLanjutkan == "y":
            display()
        elif isLanjutkan == "n":
            print("BYE!")
            exit()
        else:
            print("Masukan 'y' / 'n'")


HitungLuas()
