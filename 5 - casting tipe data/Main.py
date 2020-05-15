# kita coba belajar Casting
# merubah dari satu tipe ke tipe lain
#  tipe data = int, float, str, bool

print("="*4, "Integer", "="*4)
# INTEGER
data_int = 9
print("data = ", data_int, ",type = ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)  # akan False jika angka int adalah 0
print("data = ", data_float, ",type = ", type(data_float))
print("data = ", data_bool, ",type = ", type(data_bool))
print("data = ", data_str, "'type = ", type(data_str))

print("="*4, "Float", "="*4)
# FLOAT
data_float = 9.5
print("data = ", data_float, ",type = ", type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)  # akan False jika angka int adalah 0
print("data = ", data_int, ",type = ", type(data_int))
print("data = ", data_bool, ",type = ", type(data_bool))
print("data = ", data_str, "'type = ", type(data_str))
