# Pracovní list č. 10
import random
# # 01 nakupy.py


# def nakupy():
#     prvni_nakup = random.randint(100, 300)
#     druhy_nakup = random.randint(100, 300)
#     treti_nakup = random.randint(100, 300)
#     celkem=prvni_nakup+druhy_nakup+treti_nakup
#     print("Tvůj první nákup stál", prvni_nakup, "korun.")
#     print("Tvůj druhý nákup stál", druhy_nakup, "korun.")
#     print("Tvůj třetí nákup stál", treti_nakup, "korun.")
#     print("Celkem jsi zaplatil", celkem, "korun.")
# nakupy()
## 02 baliky.py
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
def baliky():
    x=10
    y=200
    sirka=100
    vyska=random.randint(10, 200)
    canvas.create_rectangle(x, y, x+sirka, y+vyska, fill='light green')
    canvas.create_rectangle(x+sirka, y, x+sirka, y+vyska, fill='red') 
    # canvas.create_rectangle(x+sirka+sirka, y, x+sirka, y+vyska, fill='green')

baliky()
canvas.mainloop()

## 03 text grafika.py

# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# canvas.create_text(150, 50, text='posílám pozdrav z grafické plochy')
# canvas.mainloop()

## 04 okraje.py