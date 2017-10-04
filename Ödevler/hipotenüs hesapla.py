print("bir dik üçgenin iki kenarını giriniz.\n")

a = int(input("birinci kenarı girin: "))

b= int(input("ikinci kenarı girin: "))

hip= a**2 + b**2

hipotenus = hip**(1/2)

print("Hipotenüs= {}".format(hipotenus))