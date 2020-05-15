# program konversi FAHRENHEIT ke KELVIN 

fahrenheit = int(input("Masukan satuan fahrenheit: "))

# mengkonversi ke CELCIUS
celcius = (fahrenheit - 32) / (5/9)

# dikonversi ke kelvin
kelvin = celcius + 273

print("Besar satun dalam KELVIN: ", kelvin)