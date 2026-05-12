# Pracovní list č. 18

## 01+02+03+04
##cv01 

# a = int(input("Napiš číslo:"))

# if a < 0:
#     print("Absolutní hodnota", a, "je", -a)
# else:
#     print("Absolutní hodnota", a, "je", a)

##cv03
# n = 0

# if n == 0:
#     print("Nulou dělit neumím")
# else:
#     print("1 /", n, "=", 1/n)

##cv04  stejna_cisla.py

# x=int(input("Napiš 1. číslo:"))
# y=int(input("Napiš 2. číslo:"))

# if x==y:
#     print("Čísla jsou stejná.")
#     print("pro x=", x,",", "pro y=", y)
# else:
#     print("Čísla jsou různá.")
#     print("pro x=", x,",", "pro y=", y)

##cv05  obdelnik_nebo_ctverec.py

# a=int(input("Napiš 1. stranu:"))
# b=int(input("Napiš 2. stranu:"))

# if a==b:
#     print("Je to čtverec.")
#     print("pro x=", a,",", "pro y=", b)
# else:
#     print("Je to obdélník.")
#     print("pro x=", a,",", "pro y=", b)

##cv06 pocet_sestek.py
# import random
# sestky=0    
# cisla=0

# for i in range(10):
#     a=random.randint(1,6)
#     print(a)
#     if a==6:
#         sestky=sestky+1
#     else:
#         cisla=cisla+1
    
# print("padlo", sestky, "šestek a",cisla, "jiných čísel")

##cv07 stejna_za_sebou.py
# import random

# premie = 0
# predchozi = 0

# for i in range(10):
#     hod = random.randint(1, 6)
#     print(hod)
#     if hod == predchozi:
#         premie = premie + 1
#     predchozi = hod

# print("Počet prémií:", premie)

##cv08 prestupky.py
# pocet = 0

# if pocet == 0:
#     print("Hraješ férově")
# else:
#     if pocet < 3:
#         print("Máš žlutou kartu")
#     else:
#         print("Máš červenou kartu")



##cv09 kolacky.py
# for i in range(10):
#     kolacky=int(input("kolik koláčků:"))
#     if kolacky >19:
#         print("Soutěžící je expert")
#     else:  
#         if kolacky >9:
#             print("Soutěžící je pokročilý")
#         else:
#             print("Soutěžící je začátečník")


##cv10 sklonovani.py
# import random

# n = random.randint(1,6)

# if n == 1:
#     print("Padla", n, "šestka")
# else:
#     if n < 5:
#         print("Padly", n, "šestky")
#     else:
#         print("Padlo", n, "šestek")
##cv11 porovnani_veku.py

# ja=int(input("Napiš svůj věk:"))
# ona=int(input("Napiš věk kamarádky:"))

# if ja==ona:
#     print("Jsme stejně staří")
# else:
#     if ja < ona:
#         print("Jsem mladší")
#     else:
#         print("Ona je starší")

##cv12 nemecka_vlajka.py

import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

r = 5

for i in range(5000):
    x = random.randint(10, 350)
    y = random.randint(10, 250)
    if y < 90:
        barva = "black"
    else:
        if y < 170:
            barva = "red"
        else:
            barva = "yellow"
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=barva, outline="black")

canvas.mainloop()
