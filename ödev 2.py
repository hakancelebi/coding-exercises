ad = input("Adınız: ")
soyad = input("Soyadınız: ")

kilosu = kilo = int(input("Kilonuz: "))
boyu = boy = float(input("Boyunuz: "))



print("Beden kitle endeksiniz hesaplanıyor....")



indeks = kilo // boy

bilgiler = [ad,soyad,kilo,boy,indeks]

print("Adınız: {} \nSoyadınız: {} \nKilonuz: {} \nBoyunuz: {} \nBeden Kitle Endeksiniz: {}".format(bilgiler[0],bilgiler[1],bilgiler[2],bilgiler[3],bilgiler[4]))

print("Beden kitle endeksiniz hesaplandı....")
















