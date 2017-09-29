print("Oyuncu Kaydetme Programına Hoş Heldiniz!")

ad = input("Oyuncunun adı: ")
soyad = input("Oyuncunun Soyadı: ")
takım = input("Oyuncunun takımı: ")

bilgiler = [ad, soyad, takım]

print("Bilgiler kayıt ediliyor")

"""print("bilgiler {}{}{}".format(bilgiler[0], bilgiler[1], bilgiler[2]), ad, soyad, takım)"""


print("Oyuncu adı: {}\nOyuncu soyadı: {}\nOyuncunun takımı {} \n".format(bilgiler[0], bilgiler[1], bilgiler[2]))

print("Bilgiler kaydedildi...")

