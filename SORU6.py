sene=int(input("Sene giriniz:"))
def yuzyil_hesabi(yil):
    return (yil - 1) // 100 + 1
print(yuzyil_hesabi(sene))
