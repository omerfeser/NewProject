with open("deneme.txt","r") as f:
    icerik = f.readlines()
    print(icerik)
    for i in icerik:
        print(i,end="")

