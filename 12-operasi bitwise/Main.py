# 
# 
#  @author akm.mp
# 
# 

a = 9
b = 5

# Bitwise OR (|)
c = a | b
print("========OR===========")
print("nilai a : ", a, ", binary : ", format(a, '08b'))
print("Nilai b : ", b, ", binary : ", format(b, '08b'))
print("-------------------------------------(|)")
print("nilai c : ", c, ", binary : ", format(c, '08b'))


# bitwise AND (&)
c = a & b
print("========AND===========")
print("nilai a : ", a, ", binary : ", format(a, '08b'))
print("Nilai b : ", b, ", binary : ", format(b, '08b'))
print("-------------------------------------(&)")
print("nilai c : ", c, ", binary : ", format(c, '08b'))


# bitwise XOR (^)
c = a ^ b
print("========XOR===========")
print("nilai a : ", a, ", binary : ", format(a, '08b'))
print("Nilai b : ", b, ", binary : ", format(b, '08b'))
print("-------------------------------------(^)")
print("nilai c : ", c, ", binary : ", format(c, '08b'))


# bitwsie NOT (~)
c = ~a
print("========NOT===========")
print("nilai a : ", a, ", binary : ", format(a, '08b'))
print("-------------------------------------(~)")
print("nilai c : ", c, ", binary : ", format(c, '08b'))
print("-------------------------------------(^)")
d = 0b0000001001
e = 0b1111111111
print("nilai : " ,e^d, "binary : ", format(e^d,"08b"))



# SHIFTING


# shifting right (>>)
c = a >> 2
print("========>>===========")
print("nilai a : ", a, ", binary : ", format(a, '08b'))
print("Nilai b : ", b, ", binary : ", format(b, '08b'))
print("-------------------------------------(^)")
print("nilai c : ", c, ", binary : ", format(c, '08b'))


# shifting left (<<)
c = b << 2
print("========<<===========")
print("nilai a : ", a, ", binary : ", format(a, '08b'))
print("Nilai b : ", b, ", binary : ", format(b, '08b'))
print("-------------------------------------(^)")
print("nilai c : ", c, ", binary : ", format(c, '08b'))




