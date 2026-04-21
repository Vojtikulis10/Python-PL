# Pracovní list č. 11

## 01 gps.py 

# import tkinter
# import random
# canvas = tkinter.Canvas()
# canvas.pack()

# def gps():
#     x = random.randint(10, 300)  
#     y = random.randint(10, 200)
#     canvas.create_text(x, y, text='+')
#     canvas.create_text(x - 10, y + 10, text=x)
#     canvas.create_text(x + 10, y + 10, text=y)
# gps()
# gps()
# gps()
# gps()
# gps()
# gps()
# gps()
# gps()
# gps()
# gps() 
# canvas.mainloop()

## a tak dále pokračujte

## 02 tesim_se.py 

# print('Těším se na prázdniny')
# print('Těším se na prázdniny')
# print('Těším se na prázdniny')
# print('Těším se na prázdniny')
# print('Těším se na prázdniny')

## 03 tesim_se_upraven.py 

# for i in range (5) :
#     print('Těším se na prázdniny')

## 05 tesim_se_upraven.py
# for i in range (5) :
#     print('Těším se na prázdniny')
#     print('=====================')

## 07 gps_upraven.py

# import tkinter
# import random
# canvas = tkinter.Canvas()
# canvas.pack()

# def gps():
#     x = random.randint(10, 300)  
#     y = random.randint(10, 200)
#     canvas.create_text(x, y, text='+')
#     canvas.create_text(x - 10, y + 10, text=x)
#     canvas.create_text(x + 10, y + 10, text=y)
# for i in range (10) :
#     gps()
# canvas.mainloop()

## 08 opakovany_ctverec.py

# import tkinter
# import random
# canvas = tkinter.Canvas()
# canvas.pack()

# def cerveny_ctverec():
#     x = random.randint(10, 350)  
#     y = random.randint(10, 250)
#     canvas.create_rectangle(x, y, x+10, y+10, fill="red")
# for i in range (2000) :
#     cerveny_ctverec()
# canvas.mainloop()

## 09 opakovany_ctverec_upraven.py
# import tkinter
# import random
# canvas = tkinter.Canvas()
# canvas.pack()

# def cerveny_ctverec():
#     x = random.randint(10, 350)  
#     y = random.randint(10, 250)
#     canvas.create_rectangle(x, y, x+10, y+10, fill="red")
# def modry_ctverec():
#     x = random.randint(10, 350)  
#     y = random.randint(10, 250)
#     canvas.create_rectangle(x, y, x+10, y+10, fill="blue")
# for i in range (2000) :
#     cerveny_ctverec()
#     modry_ctverec()
# canvas.mainloop()

## 10 opakovany_ctverec_upraven.py

# import tkinter
# import random
# canvas = tkinter.Canvas()
# canvas.pack()

# def cerveny_ctverec():
#     x = random.randint(10, 350)  
#     y = random.randint(10, 250)
#     canvas.create_rectangle(x, y, x+10, y+10, fill="red")
# def modry_ctverec():
#     x = random.randint(10, 350)  
#     y = random.randint(10, 250)
#     canvas.create_rectangle(x, y, x+10, y+10, fill="blue")
# for i in range (2000) :
#     cerveny_ctverec()
# for i in range (2000) :
#     modry_ctverec()
# canvas.mainloop()

## 11 obloha.py
# import tkinter
# import random
# canvas = tkinter.Canvas()
# canvas.pack()

# canvas.create_rectangle(0, 0, 380, 270, fill='navy')
# def hvezdicka():
#     x = random.randint(10, 360)
#     y = random.randint(10, 250)
#     a = random.randint(2, 4)
#     canvas.create_rectangle(x, y, x + a, y + a, fill='yellow')
# for i in range(1000):
#  hvezdicka()

# canvas.mainloop()

## 12 proogram_cislo.py

# import random
# for i in range(5):
#  n = random.randint(1, 100)
#  print('bylo vylosováno číslo', n)

## 13 dve_kostky.py

# import random
# for i in range(5):
#  n = random.randint(1, 100)
#  m = random.randint(1, 100)
#  print('Na první kostce padlo číslo', n)
#  print('Na druhé kostce padlo číslo', m)
#  print('Součet obou čísel je', n+m)

## 14 kostky_s_cisly.py
# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# import random
# for i in range(5):
#  x = random.randint(60, 330)
#  y = random.randint(60, 210)
#  canvas.create_rectangle(x - 50, y - 50, x + 50, y + 50,
#  fill='white')
#  canvas.create_text(x, y, text=random.randint(1, 6), font='arial 50')

# canvas.mainloop()

## 15 qr_kod.py

import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()
for i in range(250):
 x = random.randint(1, 21) * 10
 y = random.randint(1, 21) * 10
 canvas.create_rectangle(x, y, x + 10, y + 10, fill='black')

canvas.mainloop()





