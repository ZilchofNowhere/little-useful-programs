import time

ltr = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "q", "r", "s", "ş", "t", "u", "ü", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
decode = []
encode = []

while True:
    q = input('Metninizi şifrelemek için "ş", çözmek için "ç" yazın:\n')
    if q == "ş":
        x = input("Metninizi girin:\n")
        for l in x: 
            if l == "0":
                encode.append("b")
            elif l == "9":
                encode.append("a")
            elif l in ltr:
                encode.append(ltr[ltr.index(l) + 2])
            else:
                encode.append(l)
        print(*encode)
        encode = []
    elif q == "ç":
        y = input("Metninizi girin:\n")
        for l in y:
            if l == "b":
                decode.append("0")
            elif l == "a":
                decode.append("9")
            elif l in ltr:
                decode.append(ltr[ltr.index(l) - 2])
            else:
                decode.append(l)
        print(*decode)
        decode = []
    else:
        print("Geçerli bir girdi girin")
    c = input('Devam etmek için "d", çıkmak için "e" yazın:\n')
    if c == "d":
        continue
    elif c == "e":
        break
    else:
        print("Geçerli bir girdi girin")

print("Bizi kullandığınız için teşekkürler, şifrenizi gizli tutun")
time.sleep(3)