# episode latihan logika dan komparasi

# membuat area rentang dari angka

# +++++3-----------10++++++++

inputUser = float(input("Masukan angka yang bernilai\nkurang dari 3\natau \nlebih besar dari 10\n: "))

# +++++3------------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 = ", isKurangDari)


# --------10++++++++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 = ",isLebihDari)
 
# +++++++3-----------10+++++++++
isCorrect = isKurangDari or isLebihDari
print('Angka yang anda masukan: ' , isCorrect)


print("\n",10*"=","\n")


# --------3++++++++10-------
# kasus irisan

inputUser = float(input("Masukan angka yang bernilai\nlebuh dari 3\ndan \nkurang besar dari 10\n: "))

# ------3+++++++++++
# lebih dari 3
isLebihDari = (inputUser > 3)
print("Lebih dari 3 = ", isLebihDari)

# ++++++++++++10------------
isKurangDari = (inputUser < 10)
print("kurang dari 10 = ", isKurangDari)


isCorrect = isLebihDari and isKurangDari
print("angka yang anda masukan : ", isCorrect)


















