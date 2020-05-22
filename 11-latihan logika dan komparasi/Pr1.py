# membuat area rentang dari angka 

# -------0+++++++5---------8+++++++++11-------

inputUser = float(input("\nMasukan angka: "))

# -------0+++++++
isLebihDari0 = inputUser > 0
print("lebih dari 0 = ", isLebihDari0)

# +++++++++5--------
isKurangDari5 = inputUser < 5
print("Kurang dari 5 = ", isKurangDari5)

# ---------8++++++++++
islebihDari8 = inputUser > 8
print("Lebih dari 8 = ", islebihDari8)

# +++++++11---------
isKurangDari11 = inputUser < 11
print("Kurang dari 11 = ", isKurangDari11)


isCorrect = (isLebihDari0 and isKurangDari5) or (islebihDari8 and isKurangDari11)
print("Angka yang anda masukan = ", isCorrect)
