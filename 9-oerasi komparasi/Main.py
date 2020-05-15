# operasi komparai

# setiap hasil dari operasi komparasi adalah boolean

# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# lebih besar  dari (>)
print("\n== > ==")
hasil = a > b
print(hasil)
hasil = b > a
print(hasil)
hasil = a > 4
print(hasil)

# lebih kecil dari (<)
print("\n== < ==")
hasil = a < b
print("hasil")
hasil = b < a
print(hasil)
hasil = a < 4
print(hasil)

# lebih dari sama dengan (>=)
print("\n== >= ==")
hasil  = a >= b
print(hasil)
hasil = b >= a
print(hasil)
hasil = a >= 4
print(hasil)

# kurang dari sama dengan ( <= )
print("\n== <= ==")
hasil  = a <= b
print(hasil)
hasil = b <= a
print(hasil)
hasil = a <= 4
print(hasil)

# sama dengan ( == )
print("\n== == ==")
hasil  = a == b
print(hasil)
hasil = b == a
print(hasil)
hasil = a == 4
print(hasil)

# IS object identity
print("\n== is ==")
x= 5
y = 5
print(hex(id(x)))
print(hex(id(y)))
hasil = x is y
print(hasil)

x= 6
y = 5
print(hex(id(x)))
print(hex(id(y)))
hasil = x is y
print(hasil)


# IS NOT 
print("\n== is not ==")
x= 5
y = 5
print(hex(id(x)))
print(hex(id(y)))
hasil = x is not y
print(hasil)

x= 5
y = 6
print(hex(id(x)))
print(hex(id(y)))
hasil = x is not y
print(hasil)