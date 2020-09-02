print("""
******************
KULLANICI GİRİŞİ
******************
""")

sys_kullanıcı_adı = "hhakan"
sys_paraola = "12345"

kullanıcı_adı = input("Kullanıcı Adı: ")
parola = input("Parola: ")

if (kullanıcı_adı == sys_kullanıcı_adı and sys_paraola != parola):
    print("Parola Hatalı....")
elif (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_paraola):
    print("Kullancı Adı Hatalı....")
elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_paraola):
    print("Kullancı Adı veya Parola Hatalı....")
else:
    print("Sisteme Başarıyla Giriş Yapıldı.")
