kilo = int(input("Kilonuz: "))
boy = float(input("Boyunuz: "))

indeks = kilo // (boy * boy)

if (indeks < 18.5):
    print("ZAYIFSINIZ")
elif (18.5 < indeks < 25):
    print("KİLONUZ NORMAL")
elif (25 < indeks < 30):
    print("FAZLA KİLOLUSUNUZ")
else:
    print("OBEZSİNİZ")