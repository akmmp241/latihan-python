# membuat rantang area  angka

# +++++++0-------5++++++++++8----------11+++++++++


inputUser = float(input("\nMasukan angka: "))

# -------0+++++++
isKurangDari0 = inputUser < 0
print("kurang dari 0 = ", isKurangDari0)

# +++++++++5--------
isLebihDari5 = inputUser > 5
print("lebih dari 5 = ", isLebihDari5)

# ---------8++++++++++
isKurangDari8 = inputUser < 8
print("Kurang dari 8 = ", isKurangDari8)

# +++++++11---------
isLebihDari11 = inputUser > 11
print("Lebih dari 11 = ", isLebihDari11)


isCorrect = (isKurangDari0 or isLebihDari5) and (isKurangDari8 or isLebihDari11)
print("Angka yang anda masukan adalah: ", isCorrect)
