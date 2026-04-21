# Pracovní list č. 12

## 01 rikanka.py - nemusíte dělat

## 02 rada_cisel.py

# for i in range(10): 
#     print('číslo', i)

## 03 a
# for i in range(11): 
#     print('číslo', i)
## 03 b
# for i in range(1,11): 
#     print('číslo', i)
## 03 c
# for i in range(10): 
#     print('číslo',(i+1)*2)
## 03 d
# for i in range(10): 
#     print('číslo',(i+1)*10)
 
## 04 Vytvoř program druhe_mocniny.py, který pomocí for cyklu vypíše čísla a jejich 
# druhé mocniny:
# for i in range(7): 
#     print(i,'na druhou je',(i*i))

 
## 05 Máme takovouto povídku (povidka.py): 
# Na stromě bylo 0 vrabců, jeden přiletěl a už je tam 1 vrabců 
# for i in range(10): 
#     print('Na stromě bylo',i,'vrabců, jeden přiletěl a už je tam',i+1,"vrabců")

 
## 06 Vrabci z předchozí povídky odlétají 
# for i in range(10,-1, -1): 
    # print('Na stromě bylo',i,'vrabců, jeden odletěl a zůstalo tam',i,"vrabců")


## 07 Máme kartičky s čísly od 0 do 9, které chceme náhodně rozložit po ploše. Vytvoř program 
# deset_karticek.py, který pomocí cyklu postupně nakreslí deset takových kartiček na 
# náhodných pozicích

# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# import random
# for i in range(10):
#  x = random.randint(60, 330)
#  y = random.randint(60, 210)
#  canvas.create_rectangle(x - 25, y - 20, x + 25, y + 20,
#  fill='lightblue')
#  canvas.create_text(x, y, text = i, font='arial 20')

# canvas.mainloop()


## 08. Na chodníku je rozhozených pět cizokrajných bankovek s hodnotami 10, 20, 30, 40 
# a 50. Napiš program bankovky.py, který takové bankovky nakreslí pomocí for cyklu

# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# import random
# for i in range(1,6):
#  x = random.randint(60, 330)
#  y = random.randint(60, 210)
#  canvas.create_rectangle(x - 25, y - 20, x + 25, y + 20,
#  fill='lightgreen')
#  canvas.create_text(x, y, text = i*10, font='arial 20')

# canvas.mainloop()


## 09. Vytvoř nový program kresleni_cisel.py a přepiš do něj následující kód, který kreslí 
# čísla na grafickou plochu: 

# import tkinter 
# canvas = tkinter.Canvas() 
# canvas.pack() 

# for i in range(8): 
#     x = i * 50 
#     canvas.create_text(x, 100, text=i, font='arial 30') 

# canvas.mainloop()
#  hodnota v proměnné i hodnota v proměnné x
# když se zobrazí 0-i=0-x=
# když se zobrazí 1-i=1-x=50
# když se zobrazí 2-i=2-x=100
# když se zobrazí 3-i=3-x=150
# když se zobrazí 4-i=4-x=200
# když se zobrazí 5-i=5-x=250
# když se zobrazí 6-i=6-x=300
# když se zobrazí 7-i=7-x=350

## 10. Uprav předchozí program tak, aby se čísla kreslila přibližně na úhlopříčce grafické plochy 
# podobně jako na následujícím obrázku
# import tkinter 
# canvas = tkinter.Canvas() 
# canvas.pack() 

# for i in range(8): 
#     x = i * 50 
#     y = i * 35
#     canvas.create_text(x, y, text=i, font='arial 30') 

# canvas.mainloop()

## 11. Uprav předchozí program tak, aby se čísla kreslila přibližně na úhlopříčce grafické plochy 
# podobně jako na následujícím obrázku
# import tkinter 
# canvas = tkinter.Canvas() 
# canvas.pack() 

# for i in range(8): 
#     x = i * 50 +20
#     y = i * 32 +20
#     canvas.create_text(x, y, text=i, font='arial 30') 

# canvas.mainloop()

## 12 Víš, jak vypadá padající had z domina? Vytvoř program domino.py, který pomocí cyklu 
# a obdélníku nakreslí zatím ještě stojící kostky domina
# import tkinter 
# canvas = tkinter.Canvas() 
# canvas.pack() 

# for i in range(6):
#     x=i*50+10
#     canvas.create_rectangle(x, 100, x+20, 200, fill="red")

# canvas.mainloop()

## 13 Napiš program velka_pyramida.py, který pomocí cyklu a obdélníku nakreslí 
# takovouto pyramidu: 

# import tkinter 
# canvas = tkinter.Canvas() 
# canvas.pack() 

# for i in range(6):
#     x=i*+150
#     canvas.create_rectangle(x, 100, x+20, 200, fill="orange")

# canvas.mainloop()

import tkinter
canvas = tkinter.Canvas()
canvas.pack()

for i in range(10):
    canvas.create_rectangle(200 - (10-i)*10, 200 - i*20, 200 + (10-i)*10, 220 - i*20, fill="orange")

canvas.mainloop()



