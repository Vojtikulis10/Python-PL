# Pracovní list č. 13
 
## 01 druhe_mocniny_platno.py
# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
 
# for i in range(11):
#     x = i * 0 +20
#     y = i * 20 +20
#     canvas.create_text(x, y, text=i, font='arial 10')
#     canvas.create_text(x+40, y, text=i*i, font='arial 10')
# canvas.mainloop()
 
 
## 02 na papir napiste a zkontrolujte
 
# import tkinter
 
# canvas = tkinter.Canvas()
# canvas.pack()
 
# y = 10
# for i in range(11):
#     canvas.create_text(10, y, text=i)
#     y = y + 20
 
# canvas.mainloop()
 
## 03 rada_ctvercu.py
 
# import tkinter
 
# canvas = tkinter.Canvas()
# canvas.pack()
 
# x=10
# y=110
# for i in range(9):
#     canvas.create_rectangle(x,y,x+30,y+30, fill="red")
#     x=x+40
# canvas.mainloop()
 
## 04 + 05 zlaty_poklad.py s mezerami
 
# import tkinter
import random
# canvas = tkinter.Canvas()
# canvas.pack()
 
# x=10
# y=110
# for i in range(9):
#     o=random.randint(10,40)
#     canvas.create_rectangle(x,y,x+o,y-o, fill="orange")
#     x=x+o
# canvas.mainloop()
 
 
# import tkinter
# import random
# canvas = tkinter.Canvas()
# canvas.pack()
 
# x=10
# y=110
# for i in range(9):
#     o=random.randint(10,40)
#     canvas.create_rectangle(x,y,x+o,y-o, fill="gold")
#     x=x+o+5
# canvas.mainloop()
## pokračujte dle pdf
 
## 06 skore_hry.py
# h=0
# for i in range(1,11):
#     h=h+i
#     print("Po levelu", i, "bude tvé skóre", h, "bodů.")
   
## 07 zrnka_sachovnice.py
 
# celkem = 0
 
# for i in range(1, 65):
#     celkem = celkem + i * 10
 
# print("Celkový počet zrnek na šachovnici je", celkem, "zrnek.")

## 08 zrnka_sachovnice_upravena.py

# celkem = 0
# zrnka=1

# for i in range(1, 65):
#     celkem = celkem + zrnka
#     zrnka=zrnka*2
 
# print("Celkový počet zrnek na šachovnici je", celkem, "zrnek.")
 
## 09 jested.py

import tkinter

canvas = tkinter.Canvas()
canvas.pack()

x = 50
y = 150
sirka = 10
vyska = 210

for i in range(5):
    canvas.create_rectangle(x, y - vyska // 2, x + sirka, y + vyska // 2, fill="gray")
    x = x + sirka
    sirka += 10
    vyska -= 40

# anténa
canvas.create_rectangle(x, y - 5, x + 60, y + 5, fill="gray")

canvas.mainloop()
 