def isLanjutkan(start, halaman):
    mulai = True

    while mulai:
        isLanjutkan = input("\napakah anda ingin kembali? (y/n)")

        if isLanjutkan == "y":
            kembali = halaman
            print(kembali)
        elif isLanjutkan == "n":
            start = True
            mulai = False
        elif isLanjutkan == "keluar":
            exit()
        else:
            print("Masukan 'y' / 'n'")
            print("Ketikan 'keluar' jika ingin keluar")
            input("")
