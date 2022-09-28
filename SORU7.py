def clockangles(hour, minute):
        return abs((minute * 11 - hour * 60)) / 2

hour=int(input("Saat giriniz:"))
minute=int(input("Dakika giriniz:"))
print(clockangles(hour,minute))