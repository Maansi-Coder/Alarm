import datetime
from playsound import playsound

import tkinter as tk

window= tk.Tk()
window.geometry("500x250")

def alarm():
    Hour= int(clicked_h.get())
    Min= int(clicked_m.get())
    Am= clicked_am.get()
   
    if Am=="Pm":
        Hour+=12
    print(Hour)
    print(Min)
    print(Am)
    while True:
        if (Hour==datetime.datetime.now().hour and Min==datetime.datetime.now().minute):
            print("Playing....")
            playsound("alarm.mp3")
            break

l1= tk.Label(window,text="Set alarm",font="Georgia 20 italic bold")
l1.place(relx=0.35,rely=0.1)

h= list(range(1,13))
m= list(range(1,61))
am= ["Am","Pm"]

l2=tk.Label(window,text="Hour",font="bold")
l2.place(relx=0.30,rely=0.25)

clicked_h = tk.StringVar()
clicked_h.set("00")
drop = tk.OptionMenu( window , clicked_h , *h ) 
drop.place(relx=0.28,rely=0.35) 

l4=tk.Label(window,text=":",font="bold")
l4.place(relx=0.41,rely=0.35)

l3=tk.Label(window,text="Min",font="bold")
l3.place(relx=0.48,rely=0.25)

clicked_m = tk.StringVar()
clicked_m.set("00")
drop = tk.OptionMenu( window , clicked_m , *m ) 
drop.place(relx=0.45,rely=0.35) 

l5=tk.Label(window,text="Am / Pm",font="bold")
l5.place(relx=0.58,rely=0.25)

clicked_am = tk.StringVar()
clicked_am.set("00")
drop = tk.OptionMenu( window , clicked_am , *am ) 
drop.place(relx=0.60,rely=0.35) 

b= tk.Button(window,text="Set",font="Georgia 15 italic bold",command=alarm)
b.place(relx= 0.45,rely=0.6)
  
b2=tk.Button(window,text="Stop",font="Georgia 15 italic bold",command=window.destroy)
b2.place(relx= 0.43,rely= 0.8)

        
window.mainloop()