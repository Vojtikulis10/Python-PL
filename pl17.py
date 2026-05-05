# cv01 pozdravy_podle_veku.py
# vek=40
# vek=int(input("Zadej věk: "))
# if vek < 30:
#     print("Ahoj")
# else:
#     print("Dobrý den")

# cv02 brigada.py

# hodin= int(input("Napiš kolik hodin jsi odpracoval:"))
# if hodin <10:
#     print("Vyděláš si", hodin*80, "korun.")
# else:
#     print("Vyděláš si", hodin*100, "korun.")

# cv03 brigada.py

# hodin= int(input("Napiš kolik hodin jsi odpracoval:"))
# if hodin <10:
#  mzda = hodin*80
# else:
#  mzda = hodin*100
# print('Vyděláš si', mzda, 'korun.')

# cv04 mobilni_data.py

# data= int(input("Přenesená data:"))
# if data <10:
#  print("Zaplatíš", data*2, "korun.")
# else:
#  print("Zaplatíš 20 korun.")

# cv05 mobilni_data2.py

# data= int(input("Přenesená data:"))
# if data <10:
#  print("Zaplatíš", data, "korun.")
# else:
#  print("Zaplatíš", 10+(data-10)*3, "korun.")

# cv6 den_noc.py
# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# x=170
# y=60
# r=70
# # cas= int(input("Kolik je hodin:"))
# cas= 14
# if cas < 8:
#     canvas.create_oval(x, y,x+r,y+r, fill="white")
# else:
#     canvas.create_oval(x, y,x+r,y+r, fill="yellow")

# canvas.mainloop()

#cv07 den_noc2.py

# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# x=170
# y=60
# r=70
# # cas= int(input("Kolik je hodin:"))
# cas= 14
# if cas < 8:
#     canvas.create_rectangle(0,0,400,300,fill='navy')
#     canvas.create_oval(x, y,x+r,y+r, fill="white")
# else:
#     canvas.create_rectangle(0,0,400,300,fill='cyan')
#     canvas.create_oval(x, y,x+r,y+r, fill="yellow")

# canvas.mainloop()

#cv07 den_noc2.py

# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# x=200
# y=150
# r=50
# # cas= int(input("Kolik je hodin:"))
# cas=14
# if cas < 8:
#     canvas.create_rectangle(0,0,400,300,fill='navy')
#     canvas.create_oval(x-r, y-r,x+r,y+r, fill="white")
# else:
#     canvas.create_rectangle(0,0,400,300,fill='cyan')
#     canvas.create_oval(x-r, y-r,x+r,y+r, fill="yellow")
# canvas.create_rectangle(0,180,400,300,fill='green')
# canvas.mainloop()

#cv08 a 09 den_noc3.py
# import random
# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()

# x=random.randint(100,300)
# y=random.randint(100,200)
# r=50
# # cas= int(input("Kolik je hodin:"))
# cas= random.randint(0,16)
# if cas < 8:
#     canvas.create_rectangle(0,0,400,300,fill='navy')
#     canvas.create_oval(x-r, y-r,x+r,y+r, fill="white")
# else:
#     canvas.create_rectangle(0,0,400,300,fill='cyan')
#     canvas.create_oval(x-r, y-r,x+r,y+r, fill="yellow")
# canvas.create_rectangle(0,180,400,300,fill='green')
# canvas.mainloop()

##cv10 
# for i in range(8):
#  print(i, 'ještě spím')
# for i in range(6):
#  print(8 + i, 'jsem ve škole')

##cv11 chudy_bohaty.py
# for i in range(0,91,10):
#     if i < 50:
#         print('Mám', i, 'korun, jsem chudý')
#     else:
#         print('Mám', i , 'korun, jsem bohatý')

#cv12 nasobky_peti.py

# for n in range(11):
#     n2 = n * n
#     n = 5 * n
#     if n2 < n:
#         print(n2, "je menší než", n)
#     else:
#         print(n2, "je větší nebo rovno", n)

#cv13 koralky_na_niti.py

# import random
# import tkinter
# canvas = tkinter.Canvas(width=700, height=150)
# canvas.pack()

# x=50
# y=75
# r=20

# for i in range(15):
#     if i < 8:
#         canvas.create_oval(x-r, y-r,x+r,y+r, fill="red")
#         x=x+2*r
#     else:
#         canvas.create_oval(x-r, y-r,x+r,y+r, fill="blue")
#         x=x+2*r

# canvas.mainloop()

#cv14 koralky_na_niti.py

# import random
# import tkinter
# canvas = tkinter.Canvas(width=700, height=150)
# canvas.pack()

# x=50
# y=75
# r=20

# for i in range(15):
#     if i < 8:
#         canvas.create_oval(x-r, y-r,x+r,y+r, fill=random.choice(['red', 'yellow']))
#         x=x+2*r
#     else:
#         canvas.create_oval(x-r, y-r,x+r,y+r, fill=random.choice(['blue', 'green']))
#         x=x+2*r

# canvas.mainloop()

#cv15 rozsypane_koralky.py

import tkinter
import random

canvas = tkinter.Canvas(width=400, height=300)
canvas.pack()

r = 10

def koralek():
    x = random.randint(r, 400-r)
    y = random.randint(r, 300-r)
    if x < 200:
        barva = random.choice(["red", "yellow"])
    else:
        barva = random.choice(["blue", "green"])
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=barva)

for i in range(200):
    koralek()

canvas.mainloop()
