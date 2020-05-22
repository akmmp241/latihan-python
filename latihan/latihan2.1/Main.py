from Tool.clc import clc
from Tool.jeda import jeda
from Tool.isLanjutkan import isLanjutkan
from Module.Persegi import persegi 
from Module.persegipanjang import persegipanjang
from Module.Lingkaran import lingkaran

def HitungLuas():
    start = True

    while start:
        clc()
        print("\t"*3,"HitungLuas\n")
        print("1.persegi")
        print("2.persegi panjang")
        print("3.lingkaran")
        print("0.keluar")

        menu = input("\nMasukan pilihan: ")

        if menu == "1":
            # ini persegi
            persegi()
            start = isLanjutkan()
            break
        elif menu == "2":
            # persegipanjang()
            persegipanjang()
            break
        elif menu == "3":
            # lingkaran()
            lingkaran()
            break
        elif menu == "0":
            print("BYE")
            exit()
        else:
            print("\nMenu tidak ditemukan")
            jeda()
            
        # start = isLanjutkan()
        
        
HitungLuas()