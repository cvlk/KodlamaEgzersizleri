sayi1= int(input("1. sayıyı giriniz: "))
sayi2= int(input("2. sayıyı giriniz: "))
sayi3= int(input("3. sayıyı giriniz: "))

if(sayi1>sayi2 and sayi1>sayi3):
    print("en büyük sayı 1. girdiğiniz sayı {}".format(sayi1))
elif(sayi2>sayi1 and sayi2>sayi3):
    print("en büyük sayı 2. girdiğiniz sayı {}".format(sayi2))
else:
    print("en büyük sayı 3. girdiğiniz sayı: {}".format(sayi3))