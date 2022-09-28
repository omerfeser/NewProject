n=int(input("Sayı Giriniz:"))
print("Sayının Tam Bölenleri:")
for i in range(1,n+1):
    if(n%i==0):
        print(i)


