
print("İSTANBUL GİRESUN ARASI YAKIT TÜKETİMİ VE ÜCRET HESAPLAMA")

input("Aracınızın Markası: ")
input("Aracnızın Modeli: ")

a = int(input("İstanbul Giresun Arası Kaç Km: "))

b = float(input("Aracınız Km başına kaç kr yakıyor: "))

c = a * b

bilgiler = [a, b, c]

print("istanbul Giresun Arası Kaç Km: {}\nAracınız Km Başına Kaç Kr Yakıyor: {}\nÖdemeniz Gereken Yakıt Ücreti: {} TL\n".format(a,b,c))

