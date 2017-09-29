a = int(input("a değerini giriniz: "))
b= int(input("b değeriniz giriniz: "))
c= int(input("c değerini giriniz: "))

delta = b**2 - 4* a* c

x1 = (-b - delta**0.5) / (2 * a)
x2 = (-b + delta**0.5) / (2 * a)

"""print( "Birinci kök: {}\nİkinci kök: {}".format([x1],[x2])) //aslında aynı şey"""

print( "Birinci kök: {}\nİkinci kök: {}".format(x1,x2))