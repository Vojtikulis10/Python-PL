# Pracovní list č. 7

## 01 dotykajici.py

# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# canvas.create_rectangle(50, 50, 150, 150, fill='red') 
# canvas.create_rectangle(150, 150, 250, 250, fill='blue') 
# canvas.mainloop()

## 02 pozice_promenne.py

# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# x = 100
# y = 70
# canvas.create_rectangle(x, y, x + 100  , y+100   , fill='yellow') 
# canvas.mainloop()

## 03 obdelnik_promenne.py 

# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# x = 100
# y = 70
# sirka=200
# vyska=50
# canvas.create_rectangle(x, y, x + sirka  , y+vyska   , fill='red') 
# canvas.mainloop()

## 04 levy_roh.py

# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# x = 50
# y = 30
# delkac=100
# delkam=70
# delkatm=40
# canvas.create_rectangle(x, y, x+delkac , y+delkac , fill='red') 
# canvas.create_rectangle(x, y, x+delkam , y+delkam , fill='blue') 
# canvas.create_rectangle(x, y, x+delkatm , y+delkatm , fill='darkblue') 
# canvas.mainloop()

## 05 vedle_sebe.py

# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# x = 15
# y = 40
# a=120
# b=70
# canvas.create_rectangle(x, y, x+a , y+b , fill='blue') 
# canvas.create_rectangle(x+a, y, x+a+a , y+b , fill='lightblue') 
# canvas.create_rectangle(x+a+a, y, x+a+a+a , y+b , fill='darkblue') 
# canvas.mainloop()

## 06 stred_ctverce.py

# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# x = 100
# y = 100
# a=100
# canvas.create_rectangle(x-a/2, y-a/2, x+a/2 , y+a/2 , fill='green') 
# canvas.mainloop()

## 07 tri_soustredne.py

# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# x = 175
# y = 125
# delkac=100
# delkam=60
# delkab=20
# canvas.create_rectangle(x-delkac/2, y-delkac/2, x+delkac/2 , y+delkac/2 , fill='red') 
# canvas.create_rectangle(x-delkam/2, y-delkam/2, x+delkam/2 , y+delkam/2 , fill='blue') 
# canvas.create_rectangle(x-delkab/2, y-delkab/2, x+delkab/2 , y+delkab/2 , fill='white') 
# canvas.mainloop()

## 08 to jsem zvedav
#a)
# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# canvas.create_rectangle(0, 0, 1, 1) #nejde vidět
# canvas.mainloop()
#b)
# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# canvas.create_rectangle(10, 20, 30, 40)
# canvas.mainloop()
#c)
# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# canvas.create_rectangle(100, 150, 150, 100)
# canvas.mainloop()
#d)
# x=100
# y=100
# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# canvas.create_rectangle(x, y - 50, x + 50, y) 
# canvas.mainloop()
#e)
# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# canvas.create_rectangle(100 - 20, 70 - 30, 100 + 30, 70 + 
# 20)
# canvas.mainloop()

## 09 stred_obdelniku.py

# import tkinter
# canvas = tkinter.Canvas()
# canvas.pack()
# x=105
# y=70
# a=100
# b=125
# canvas.create_rectangle(x, y, x+a, y+b)
# canvas.mainloop()

## 10 nemusíte dělat


## 11 rada_ctvercu.py musíte dělat

import tkinter
canvas = tkinter.Canvas()
canvas.pack()
x=30
y=220
a=100
b=80
c=60
d=40
e=20
canvas.create_rectangle(x, y, x+(a+b+c+d+e), y-e, fill='blue')
canvas.create_rectangle(x, y, x+(a+b+c+d), y-d, fill='pink')
canvas.create_rectangle(x, y, x+(a+b+c), y-c, fill='green')
canvas.create_rectangle(x, y, x+(a+b), y-b, fill='yellow')
canvas.create_rectangle(x, y, x+a, y-a, fill='red')
canvas.mainloop()