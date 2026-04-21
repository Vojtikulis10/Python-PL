# Pracovní list č. 16

## 01 semafor_velky.py

## 02 nahodny_pozdrav.py

## 03+4 je třeba spustit python terminál abyste viděli >>>

## 05+6+7

# teplota = 25 
# print('Je', teplota, 'stupňů.') 
# if teplota > 20: 
#     print('Dnes je teplo.') 
# else: 
#     print('Dnes je zima.') 
# print('Správně se obleč.')


## 08 cena_dopisu.py

## 09 zmrzlina.py

## 10+11 novy_velky_semafor.py


## 12 krabice.py

## 13 kruhy_nad_sebou.py 

import tkinter
canvas = tkinter.Canvas()
canvas.pack()

x = 100
y =100
r=50
canvas.create_oval(x, y , x + r, y + r)
canvas.create_oval(x , y , x - r, y +r )


canvas.mainloop()