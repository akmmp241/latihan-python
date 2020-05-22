# import python library
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
        # menu
        print("\t"*3,"HitungLuas\n")
        print("1.persegi")
        print("2.persegi panjang")
        print("3.lingkaran")
        print("0.keluar")

        menu = input("\nMasukan pilihan: ")

        if menu == "1":
            # ini persegi
            persegi()
            pass
        elif menu == "2":
            # persegipanjang()
            persegipanjang()
            pass
        elif menu == "3":
            # lingkaran()
            lingkaran()
            pass
        elif menu == "0":
            exit()
        else:
            print("\nMenu tidak ditemukan")
            jeda()
            continue
            
        start = isLanjutkan()
        
        
HitungLuas()