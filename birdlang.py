vow = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
res = ""

while True:
    k = input("Kelime veya cümlenizi girin\n").lower()
    for l in k:
        if l in vow:
            res = res + l + "g" + l
        else:
            res = res + l
    print(f"Girdinizin kuş dili hali {res}")
    res = ""
    end = input('Devam etmek için "d" yazın, çıkmak için enter\'a basın\n')
    if end.lower() == "d":
        continue
    else:
        break