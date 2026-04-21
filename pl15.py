
# Pracovní list č. 15

## 01 dve_kruznice.py

# import tkinter

# canvas = tkinter.Canvas()
# canvas.pack()

# x = 200
# y = 100
# r = 50

# canvas.create_oval(x - 2*r, y - r, x, y + r)
# canvas.create_oval(x, y - r, x + 2*r, y + r)

# canvas.mainloop()

## 02 upravene dve_dve_kruznice.py
# import tkinter

# canvas = tkinter.Canvas()
# canvas.pack()

# x = 200
# y = 100
# r1 = 50
# r2=25

# canvas.create_oval(x - 2*r1, y - r1, x, y + r1)
# canvas.create_oval(x, y - r2, x + 2*r2, y + r2)

# canvas.mainloop()
## 03 terc.py

# import tkinter

# canvas = tkinter.Canvas()
# canvas.pack()

# x =200
# y = 125
# r1 = 10

# for i in range(1, 10):
#     canvas.create_oval(x - r1, y - r1, x+ r1, y + r1)
#     r1=r1+10
    

# canvas.mainloop()

## 04 gramovon.py
# import tkinter

# canvas = tkinter.Canvas()
# canvas.pack()

# x =200
# y = 125
# r1 = 2

# for i in range(1, 50):
#     canvas.create_oval(x - r1, y - r1, x+ r1, y + r1)
#     r1=r1+2
    

# canvas.mainloop()
## 05 upraveny terc.py
# import tkinter

# canvas = tkinter.Canvas()
# canvas.pack()

# x =200
# y = 125
# r1 = 100

# for i in range(10):
#     canvas.create_oval(x - r1, y - r1, x + r1, y + r1, fill="white")
#     r1 = r1- 10

# canvas.mainloop()
## 06 upraveny terc.py
# import tkinter

# canvas = tkinter.Canvas()
# canvas.pack()

# x =200
# y = 125
# r1 = 100

# for i in range(5):
#     canvas.create_oval(x - r1, y - r1, x + r1, y + r1, fill="white")
#     r1 = r1- 10
#     canvas.create_oval(x - r1, y - r1, x + r1, y + r1, fill="black")
#     r1 = r1 - 10

# canvas.mainloop()
## 07 retizek.py
# import tkinter

# canvas = tkinter.Canvas()
# canvas.pack()

# x = 30
# y = 150
# r = 10

# for i in range(15):
#     canvas.create_oval(x - r, y - r, x + r, y + r, fill="gold")
#     x = x + 2 * r

# canvas.mainloop()
## 08 mince.py
# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# import random

# for i in range(10):
#  x = random.randint(60, 330)
#  y = random.randint(60, 210)
#  o=random.randint(1,5)
#  canvas.create_oval(x - 25, y - 25, x + 25, y + 25,
#  fill='grey')
#  canvas.create_text(x, y, text = o, font='arial 20')

# canvas.mainloop()
## 09 upravene mince.py
# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# import random

# for i in range(10):
#  x = random.randint(60, 330)
#  y = random.randint(60, 210)
#  o=random.choice([1,2,5,10,20,50])
#  canvas.create_oval(x - 25, y - 25, x + 25, y + 25,
#  fill='grey')
#  canvas.create_text(x, y, text = o, font='arial 20')

# canvas.mainloop()
## 10 random_choice.py
# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# import random

# for i in range(10):
#  x = random.randint(60, 330)
#  y = random.randint(60, 210)
#  o=random.choice([1,2,5,10,20,50])
#  barva=random.choice(["white", "grey", "gold"])
#  canvas.create_oval(x - 25, y - 25, x + 25, y + 25,
#  fill=barva)
#  canvas.create_text(x, y, text = o, font='arial 20')

# canvas.mainloop()
## 11
import random
print(random.choice(['Ahoj', 'Nazdar', 'Servus', 'Čau']))
print(random.choice("Pomeranč"))
print(random.choice([1 / 2, 1 / 3, 1 / 4, 1 / 5]))

## 12

