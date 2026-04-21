# Pracovní list č. 14

## 01 Napiš program soucet_99.py, který pomocí cyklu zjistí, jaký je součet čísel 0 + 1 + 2 + ... + 99. Výsledek program vypíše pomocí příkazu print. 
# soucet=0
# for i in range(1, 100):
#     soucet = soucet + i
 
# print("Součet je", soucet)
## 02 2. V jazyce Python kreslíme elipsy a kruhy příkazem create_oval. Vytvoř nový program elipsa.py a zapiš do něj následující kód:
# import tkinter

# canvas = tkinter.Canvas()
# canvas.pack()

# canvas.create_oval(10, 10, 200, 150)
# canvas.mainloop()

## Vyzkoušej, co program nakreslí. 

## 03. Přidej na konec programu příkaz pro kreslení obdélníku se stejnými čísly, jako jsou v příkazu create_oval. Jaká bude vzájemná pozice elipsy a obdélníku? 
# import tkinter

# canvas = tkinter.Canvas()
# canvas.pack()

# canvas.create_oval(10, 10, 200, 150)
# canvas.create_rectangle(10, 10, 200, 150)
# canvas.mainloop()
## 04 vez.py

# import tkinter

# canvas = tkinter.Canvas()
# canvas.pack()

# canvas.create_rectangle(170, 50, 210, 90)
# canvas.create_rectangle(160, 90, 220, 150)
# canvas.create_rectangle(150, 150, 230, 230)
# canvas.mainloop()
## 05 Diskutuj se sousedem, jak nakreslit kruh. Potom změň předchozí program tak, aby se místo věže kreslil sněhulák. 

import tkinter

canvas = tkinter.Canvas(width=1920, height=1080)
canvas.pack()

canvas.create_oval(170, 50, 210, 90, fill="white")
canvas.create_oval(160, 90, 220, 150, fill="white")
canvas.create_oval(150, 150, 230, 230, fill="white")
canvas.mainloop()

## Nyní se vrhněte na pracovní list č. 15.