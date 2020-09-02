şekil = input("Hangi Şeklin Tipini Bulmak İstiyorsunuz: ")

if (şekil == "DÖRTGEN"):
    print("Lütfen Kenarları Sırasıyla Giriniz.")
    a = int(input("Kenar-1: "))
    b = int(input("Kenar-2: "))
    c = int(input("Kenar-3: "))
    d = int(input("Kenar-4: "))

    if (a == b and a == c and a == d):
        print("KARE")
    elif (a == c and b == d):
        print("DİKDÖRTGEN")
    else:
        print("DÖRTGEN")

elif (şekil == "ÜÇGEN"):
    print("Lütfen Kenarları Sırasıyla Giriniz.")
    a = int(input("Kenar-1: "))
    b = int(input("Kenar-2: "))
    c = int(input("Kenar-3: "))
    if (abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):
        if (a == b and a == c):
            print("Eşkenar Üçgen")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("İkizkenar Üçgen")
        else:
            print("Çeşitkenar Üçgen")
    else:
        print("Üçgen Beliirtilmiyor")
else:
    print("Geçersiz Şekil.")