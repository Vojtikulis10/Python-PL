##cv01 cifry_cisla.py

# cislo=int(input("Zadej číslo menší než 1000:"))

# if cislo <= 9:
#  print("Číslo",cislo ,"je jednociferné")
# else:
#     if cislo <= 99:
#         print("Číslo",cislo ,"je dvojciferné")
#     else:
#         print("Číslo",cislo ,"je trojciferné")

##cv02 muj_vek.py
# def jemi10():
#     vek = 10
#     print('Je mi', vek, 'let')
# def jemi20():
#     vek = 20
#     print('Je mi', vek, 'let')
# def jemi30():
#    vek = 30
#    print('Je mi', vek, 'let')

# jemi10()
# jemi20()
# jemi30()

##cv03 muj_vek_upraven.py

# def jemi(vek):
#  print('Je mi', vek, 'let')

# jemi(10)
# jemi(20)
# jemi(30)

##cv04 druha_mocnina_parametr.py   

# def vypis(x):
#  print('Číslo', x )
#  print('Umocněné na druhou se rovná', x*x)
# vypis(1)
# vypis(2)    
# vypis(3)

##cv05

# def vypis(x):
#  print('Číslo', x )
#  print('Umocněné na druhou se rovná', x*x)
#  print('Převrácená hodnota se rovná', 1/x)
# vypis(1)
# vypis(2)    
# vypis(3)

##cv06 kruh_parametr.py

# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# x=200
# y=150
# def kruh(r):
#  canvas.create_oval(x-r,y-r, x+r, y+r )
# kruh(10)
# kruh(100)
# kruh(50)

# canvas.mainloop()

##cv07 nahodny_kruh_parametr.py
# import tkinter
# import random

# canvas = tkinter.Canvas(width=400, height=300)
# canvas.pack()
# def nahodny_kruh(r):
#     x = random.randint(r, 400-r)
#     y = random.randint(r, 300-r)
#     canvas.create_oval(x-r, y-r, x+r, y+r, fill="red")

# nahodny_kruh(5)
# nahodny_kruh(30)
# nahodny_kruh(20)

# canvas.mainloop()
 
##cv08 nahodny_kruh_parametr_upraven.py

# import tkinter  
# import random

# canvas = tkinter.Canvas(width=400, height=300)
# canvas.pack()
# def nahodny_kruh(r):
#     x = random.randint(r, 400-r)
#     y = random.randint(r, 300-r)
#     canvas.create_oval(x-r, y-r, x+r, y+r, fill="red")

# for i in range(10):
#     nahodny_kruh(i)
#     nahodny_kruh(i)
#     nahodny_kruh(i)

# canvas.mainloop()

##cv09 nahodny_kruh_parametr_upraven.py

import tkinter  
import random

canvas = tkinter.Canvas(width=400, height=300)
canvas.pack()
def nahodny_kruh(r):
    x = random.randint(r, 400-r)
    y = random.randint(r, 300-r)
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="red")

for i in range(10):
    nahodny_kruh(i + 5)

canvas.mainloop()