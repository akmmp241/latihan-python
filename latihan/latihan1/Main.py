from module import tool

def HitungLuas():
    tool.clearScreen()

    print("HitungLuas\n")
    start = True

    while start:
        print("\n1.persegi")
        print("2.persegi panjang")
        print("0.keluar")

        menu = input("\nMasukan pilihan: ")

        if menu == "1":
            print("persegi")
            input("")
            tool.clearScreen()
        elif menu == "2":
            print("persegi panjang")
            input("")
            tool.clearScreen()
        elif menu == "0":
            exit()
        else:
            print("menu tidak ditemukan")
            input("")
            tool.clearScreen()

        


HitungLuas()