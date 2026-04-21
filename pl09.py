# Pracovní list č. 9


## 01 mrizka.py

# def cara():
#     print("+--+--+--+--+--+--+")
# def hulky():
#     print("|  |  |  |  |  |  |")
# cara()
# hulky()
# cara()
# hulky()
# cara()

## 02 

# def ctvereckovany_papir():
#     cara()
#     hulky()
#     cara()
#     hulky()
#     cara()
#     hulky()
#     cara()
#     hulky()
#     cara()
# ctvereckovany_papir()
## 03 haha

# import random
# random.randint(1, 6) 
## 04 kostka.py

# import random
# n = random.randint(1, 6)
# print("Na kostce padla", n

## 05 upravena kostka.py

# import random
# def hod_kostou():
#     n = random.randint(1, 6)
#     print("Na kostce padla", n)
# hod_kostou()
## 06 dvacetihranna_kostka.py
# import random
# def hod_kostou():
#     n = random.randint(1, 20)
#     print("Na kostce padla", n)
# hod_kostou()
 
## 07 nemusíte se tím trápit
## 08 taky tak
## 09 taky tak
## 10 taky tak


## 11 predpoved.py 
# import random
# def predpoved():
#     n = random.randint(-15, 35)
#     print("Dnes bude", n, "stupňů")
# predpoved()

## 12 pin.py
# import random
# def pin():
#     a = random.randint(0, 9)
#     b = random.randint(0, 9)
#     c = random.randint(0, 9)
#     d = random.randint(0, 9)
#     print("Tvůj nový PIN je", a, b, c, d)
# pin()
## 13 datumy.py
# import random
# def datum():
#     den = random.randint(1, 30)
#     mesic = random.randint(1, 12)
#     rok = random.randint(2020, 2030)
#     print("Pokoj si uklidím", den, ".",mesic, ".", rok)
# datum()

## 14 nahodny_ctverec.py

# import tkinter
# import random

# canvas = tkinter.Canvas()
# canvas.pack()

# def nahodny_ctverec():
#     x = random.randint(10, 300)  
#     y = random.randint(10, 200)
#     canvas.create_rectangle(x,  y,  x+ 50, y + 50, fill='orange')
#     x = random.randint(10, 300)  
#     y = random.randint(10, 200)
#     canvas.create_rectangle(x,  y,  x+ 50, y + 50, fill='orange')
#     x = random.randint(10, 300)  
#     y = random.randint(10, 200)
#     canvas.create_rectangle(x,  y,  x+ 50, y + 50, fill='orange')
#     x = random.randint(10, 300)  
#     y = random.randint(10, 200)
#     canvas.create_rectangle(x,  y,  x+ 50, y + 50, fill='orange')
#     x = random.randint(10, 300)  
#     y = random.randint(10, 200)
#     canvas.create_rectangle(x,  y,  x+ 50, y + 50, fill='orange')
# nahodny_ctverec()
# canvas.mainloop()

#16 
# import tkinter
# import random

# canvas = tkinter.Canvas()
# canvas.pack()

# def nahodny_ctverec():
#     x = random.randint(10, 300)  
#     y = random.randint(10, 200)
#     velikost = random.randint(10, 100)
#     canvas.create_rectangle(x,  y,  x+ velikost, y + velikost, fill='orange')
#     x = random.randint(10, 300)  
#     y = random.randint(10, 200)
#     canvas.create_rectangle(x,  y,  x+ velikost, y + velikost, fill='orange')
#     x = random.randint(10, 300)  
#     y = random.randint(10, 200)
#     canvas.create_rectangle(x,  y,  x+ velikost, y + velikost, fill='orange')
#     x = random.randint(10, 300)  
#     y = random.randint(10, 200)
#     canvas.create_rectangle(x,  y,  x+ velikost, y + velikost, fill='orange')
#     x = random.randint(10, 300)  
#     y = random.randint(10, 200)
#     canvas.create_rectangle(x,  y,  x+ velikost, y + velikost, fill='orange')
# nahodny_ctverec()
# canvas.mainloop()

#17
import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

def nahodny_ctverec():
    x = random.randint(10, 300)  
    y = random.randint(10, 200)
    velikost = random.randint(10, 100)
    canvas.create_rectangle(x,  y,  x+ velikost, y + velikost, fill='orange')
    x = random.randint(10, 300)  
    y = random.randint(10, 200)
    canvas.create_rectangle(x,  y,  x+ velikost, y + velikost, fill='orange')
    x = random.randint(10, 300)  
    y = random.randint(10, 200)
    canvas.create_rectangle(x,  y,  x+ velikost, y + velikost, fill='orange')
    x = random.randint(10, 300)  
    y = random.randint(10, 200)
    canvas.create_rectangle(x,  y,  x+ velikost, y + velikost, fill='orange')
    x = random.randint(10, 300)  
    y = random.randint(10, 200)
    canvas.create_rectangle(x,  y,  x+ velikost, y + velikost, fill='orange')
    
def nahodny_obdelnik():
    x = random.randint(10, 300)  
    y = random.randint(10, 200)
    velikosti_obdelniku_a = random.randint(10, 100)
    velikosti_obdelniku_b = random.randint(10, 80)
    canvas.create_rectangle(x,  y,  x+ velikosti_obdelniku_a, y + velikosti_obdelniku_b, fill='green')
    x = random.randint(10, 300)  
    y = random.randint(10, 200)
    canvas.create_rectangle(x,  y,  x+ velikosti_obdelniku_a, y + velikosti_obdelniku_b, fill='green')
    x = random.randint(10, 300)  
    y = random.randint(10, 200)
    canvas.create_rectangle(x,  y,  x+ velikosti_obdelniku_a, y + velikosti_obdelniku_b, fill='green')
    x = random.randint(10, 300)  
    y = random.randint(10, 200)
    canvas.create_rectangle(x,  y,  x+ velikosti_obdelniku_a, y + velikosti_obdelniku_b, fill='green')
    x = random.randint(10, 300)  
    y = random.randint(10, 200)
    canvas.create_rectangle(x,  y,  x+ velikosti_obdelniku_a, y + velikosti_obdelniku_b, fill='green')
nahodny_ctverec()
nahodny_obdelnik()
canvas.mainloop()



## a tak dále pokračujte
