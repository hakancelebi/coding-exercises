Vize1 = float(input("VİZE1 NOTUNUZ: "))
Vize2 = float(input("VİZE2 NOTUNUZ: "))
Final = float(input("FİNAL NOTUNUZ: "))

ToplamNot = (Vize1 * 0.3) + (Vize2 * 0.3) + (Final * 0.4)

print("ToplamNot: {}".format(ToplamNot))


if (ToplamNot >= 90):
    print("HARF NOTUNUZ AA")
elif (ToplamNot >= 85):
    print("HARF NOTUNUZ BA")
elif (ToplamNot >= 80):
    print("HARF NOTUNUZ BB")
elif (ToplamNot >= 75):
    print("HARF NOTUNUZ CB")
elif (ToplamNot >= 70):
    print("HARF NOTUNUZ CC")
elif (ToplamNot >= 65):
    print("HARF NOTUNUZ DC")
elif (ToplamNot >= 60):
    print("HARF NOTUNUZ DD")
else:
    print("HARF NOTUNUZ FF")
