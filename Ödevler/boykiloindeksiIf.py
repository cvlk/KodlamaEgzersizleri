boy= float(input("Boyunuzu giriniz: "))
kilo= float(input("Kilonuzu giriniz: "))

"""Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)"""

index= kilo/(boy*boy)

print("Beden Kitle İndeksiniz: {}".format(index))

if(index<18.5):
    print("zayıf")
elif(18.5<index<25):
    print("normal")
elif(25<index<30):
    print("kilolu")
else:
    print("obez")