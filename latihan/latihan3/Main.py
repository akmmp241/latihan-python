# import python library
from Tool import clc,jeda,getYesOrNo
from Module import Lingkaran,persegipanjang,Persegi,Segitiga


def HitungLuas():
    start = True

    while start:
        clc.clc()
        # menu
        print("\t"*3,"HitungLuas\n")
        print("1.persegi")
        print("2.persegi panjang")
        print("3.Segitiga")
        print("4.lingkaran")
        print("5.Trapesium")
        print("6.jajarGenjang")
        print("7.belah ketupat")
        print("8.layang-layang")
        print("0.keluar")

        menu = input("\nMasukan pilihan: ")

        if menu == "1":
            # ini persegi
            Persegi.persegi()
            pass
        elif menu == "2":
            # persegipanjang()
            persegipanjang.persegipanjang()
            pass
        elif menu == "3":
            Segitiga.segitiga()
            pass
        elif menu == "4":
            # menu lingkaran
            Lingkaran.lingkaran()
            pass
        elif menu == "0":
            exit()
        else:
            print("\nMenu tidak ditemukan")
            jeda.jeda()
            continue
            
        start = getYesOrNo.isLanjutkan()
        
        
HitungLuas()