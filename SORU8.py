liste=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

eleman = str(input("Listede aranacak elemanı giriniz:"))


if eleman in liste:

    print(liste.index(eleman))

else:
    print("Eleman listede yok")


