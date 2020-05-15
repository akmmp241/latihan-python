# program mengkonversi dari stuan KELVIN ke FAHRENHEIT

print("\nMengkonversi KELVIN ke FAHRENHEIT")

kelvin = int(input("Masukan satuan kelvin: "))

# mengkonversi ke reamur
reamur = (4/5) * (kelvin - 273)

# dikonversi ke FAHRENHEIT
fahrenheit = ((9/4) * reamur) + 32

print("Besar satuan fahrenheit adalah: ", fahrenheit)