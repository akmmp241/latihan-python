def isLanjutkan():
    isLanjutkan = input("\nApakah anda ingin melanjutkan? (y/n)? ")

    while isLanjutkan.lower() != "y" and isLanjutkan.lower() != "n":
        print("pilihlah 'y' / 'n'")
        isLanjutkan = input("\nApakah anda ingin melanjutkan? (y/n)? ")

    return isLanjutkan.lower() == "y" 
