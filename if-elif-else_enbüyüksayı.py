
Sayı1 = int(input("Lütfen Birinci Sayıyı Giriniz: "))
Sayı2 = int(input("Lütfen İkinci Sayıyı Giriniz: "))
Sayı3 = int(input("Lütfen Üçüncü Sayıyı Giriniz: "))

if (Sayı1 >= Sayı2 and Sayı1 >= Sayı3):
    print("En Büyük Sayı: ", Sayı1)
elif (Sayı2 >= Sayı1 and Sayı2 >= Sayı3):
    print("En Büyük Sayı: ", Sayı2)
elif (Sayı3 >= Sayı1 and Sayı3 >= Sayı2):
    print("En Büyük Sayı: ", Sayı3)