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
import random
sestky=0    
cisla=0

for i in range(10):
    a=random.randint(1,6)
    print(a)
    if a==6:
        sestky=sestky+1
    else:
        cisla=cisla+1
    
print("padlo", sestky, "šestek a",cisla, "jiných čísel")


























































































































