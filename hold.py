
import tkinter as tk
import sys 
import os
sys.path.append(os.path.abspath(r"F:\IPL\AUCTION"))
sys.path.append(os.path.abspath(r"F:\IPL\MVP"))
sys.path.append(os.path.abspath(r"F:\IPL\LOGO"))
sys.path.append(os.path.abspath(r"F:\IPL\PLAYER PERFORMANCE"))
sys.path.append(os.path.abspath(r"F:\IPL\POINTS TABLE"))
from PT19 import *
from PT20 import *
from PT21 import *
from PT22 import *
from PT23 import *
from MVP19 import *
from MVP20 import *
from MVP21 import *
from PIL import Image, ImageTk
from BAT2008 import *
from BAT2011 import *
from BAT2020 import *
from BAT2019 import *
from BAT2021 import *
from BOWL2019 import *
from BOWL2020 import *
from BOWL2021 import *
from AUCTION19 import *
from AUCTION20 import *
from AUCTION21 import *
from AUCUNSOLD19 import *
from AUCUNSOLD20 import *
from AUCUNSOLD21 import *
import PIL.Image
import tkvideo
from playsound import playsound
import pygame


   
root=Tk()
l = Label(root)
l.pack()
root.geometry('750x750')
root.title("IPL STATISTICS")
root.attributes('-fullscreen', True)

pygame.mixer.init()
def play():
    pygame.mixer.music.load(r'C:\Users\vsais\IPL\Music\BGM2.mp3')
    pygame.mixer.music.play(loops=-1)
def pause():
   pygame.mixer.music.pause()

def PP08():
   top= Toplevel(root)
   top.geometry("750x500")
   top.attributes('-fullscreen', True)
   C=Label(top,text='DO YOU WANT TO CHECK:',font=('bold',16),anchor=CENTER)
   C.place(x=100,y=0)


   Button(top,text= "Batting Stats", command=BT2008).pack(pady= 5)
   button= Button(top, text="Bowling Stats")
   button.pack(pady=5)

def PP09():
   top= Toplevel(root)
   top.geometry("750x500")
   top.attributes('-fullscreen', True)
   C=Label(top,text='DO YOU WANT TO CHECK:',font=('bold',16),anchor=CENTER)
   C.place(x=100,y=0)


   Button(top,text= "Batting Stats", command=BT2008).pack(pady= 5)
   button= Button(top, text="Bowling Stats")
   button.pack(pady=5)

def PP10():
   top= Toplevel(root)
   top.geometry("750x500")
   top.attributes('-fullscreen', True)
   C=Label(top,text='DO YOU WANT TO CHECK:',font=('bold',16),anchor=CENTER)
   C.place(x=100,y=0)


   Button(top,text= "Batting Stats", command=BT2008).pack(pady= 5)
   button= Button(top, text="Bowling Stats")
   button.pack(pady=5)

def PP11():
   top= Toplevel(root)
   top.geometry("750x500")
   top.attributes('-fullscreen', True)
   C=Label(top,text='DO YOU WANT TO CHECK:',font=('bold',16),anchor=CENTER)
   C.place(x=100,y=0)


   Button(top,text= "Batting Stats", command=BT2011).pack(pady= 5)
   button= Button(top, text="Bowling Stats")
   button.pack(pady=5)

def PP12():
   top= Toplevel(root)
   top.geometry("750x500")
   top.attributes('-fullscreen', True)
   C=Label(top,text='DO YOU WANT TO CHECK:',font=('bold',16),anchor=CENTER)
   C.place(x=100,y=0)


   Button(top,text= "Batting Stats", command=BT2008).pack(pady= 5)
   button= Button(top, text="Bowling Stats")
   button.pack(pady=5)

def PP13():
   top= Toplevel(root)
   top.geometry("750x500")
   top.attributes('-fullscreen', True)
   C=Label(top,text='DO YOU WANT TO CHECK:',font=('bold',16),anchor=CENTER)
   C.place(x=100,y=0)


   Button(top,text= "Batting Stats", command=BT2008).pack(pady= 5)
   button= Button(top, text="Bowling Stats")
   button.pack(pady=5)

def PP14():
   top= Toplevel(root)
   top.geometry("750x500")
   top.attributes('-fullscreen', True)
   C=Label(top,text='DO YOU WANT TO CHECK:',font=('bold',16),anchor=CENTER)
   C.place(x=100,y=0)


   Button(top,text= "Batting Stats", command=BT2008).pack(pady= 5)
   button= Button(top, text="Bowling Stats")
   button.pack(pady=5)

def PP15():
   top= Toplevel(root)
   top.geometry("750x500")
   top.attributes('-fullscreen', True)
   C=Label(top,text='DO YOU WANT TO CHECK:',font=('bold',16),anchor=CENTER)
   C.place(x=100,y=0)


   Button(top,text= "Batting Stats", command=BT2008).pack(pady= 5)
   button= Button(top, text="Bowling Stats")
   button.pack(pady=5)

def PP16():
   top= Toplevel(root)
   top.geometry("750x500")
   top.attributes('-fullscreen', True)
   C=Label(top,text='DO YOU WANT TO CHECK:',font=('bold',16),anchor=CENTER)
   C.place(x=100,y=0)


   Button(top,text= "Batting Stats", command=BT2008).pack(pady= 5)
   button= Button(top, text="Bowling Stats")
   button.pack(pady=5)

def PP17():
   top= Toplevel(root)
   top.geometry("750x500")
   top.attributes('-fullscreen', True)
   C=Label(top,text='DO YOU WANT TO CHECK:',font=('bold',16),anchor=CENTER)
   C.place(x=100,y=0)


   Button(top,text= "Batting Stats", command=BT2008).pack(pady= 5)
   button= Button(top, text="Bowling Stats")
   button.pack(pady=5)

def PP18():
   top= Toplevel(root)
   top.geometry("750x500")
   top.attributes('-fullscreen', True)
   C=Label(top,text='DO YOU WANT TO CHECK:',font=('bold',16),anchor=CENTER)
   C.place(x=100,y=0)


   Button(top,text= "Batting Stats", command=BT2008).pack(pady= 5)
   button= Button(top, text="Bowling Stats")
   button.pack(pady=5)


def PP19():
   top= Toplevel(root)
   top.geometry("750x500")
   top.attributes('-fullscreen', True)
   C=Label(top,text='DO YOU WANT TO CHECK:',font=('bold',16),anchor=CENTER)
   C.place(x=100,y=0)


   Button(top,text= "Batting Stats", command=BT2019).pack(pady= 5)
   button= Button(top, text="Bowling Stats", command=BO2019)
   button.pack(pady=5)

def PP20():
   top= Toplevel(root)
   top.geometry("750x500")
   t
   C=Label(top,text='DO YOU WANT TO CHECK:',font=('bold',16),anchor=CENTER)
   C.place(x=100,y=0)


   Button(top,text= "Batting Stats", command=BT2020).pack(pady= 5)
   button= Button(top, text="Bowling Stats", command=BO2020)
   button.pack(pady=5)

def PP21():
   top= Toplevel(root)
   top.geometry("750x500")
   C=Label(top,text='DO YOU WANT TO CHECK:',font=('bold',16),anchor=CENTER)
   C.place(x=100,y=0)


   Button(top,text= "Batting Stats", command=BT2021).pack(pady= 5)
   button= Button(top, text="Bowling Stats", command=BO2021)
   button.pack(pady=5)

def PP22():
   top= Toplevel(root)
   top.geometry("750x500")
   top.attributes('-fullscreen', True)
   C=Label(top,text='DO YOU WANT TO CHECK:',font=('bold',16),anchor=CENTER)
   C.place(x=100,y=0)


   Button(top,text= "Batting Stats", command=BT2008).pack(pady= 5)
   button= Button(top, text="Bowling Stats")
   button.pack(pady=5)

def PP23():
   top= Toplevel(root)
   top.geometry("750x500")
   top.attributes('-fullscreen', True)
   C=Label(top,text='DO YOU WANT TO CHECK:',font=('bold',16),anchor=CENTER)
   C.place(x=100,y=0)


   Button(top,text= "Batting Stats", command=BT2008).pack(pady= 5)
   button= Button(top, text="Bowling Stats")
   button.pack(pady=5)

def A21():
   top= Toplevel(root)
   top.geometry("750x500")
   C=Label(top,text='DO YOU WANT TO CHECK:',font=('bold',16),anchor=CENTER)
   C.place(x=100,y=0)

   Button(top,text= "Sold Players", command=AUC2021).pack(pady= 5)
   button= Button(top, text="Unsold Players", command=AUCUN2021)
   button.pack(pady=5)

def A20():
   top= Toplevel(root)
   top.geometry("750x500")
   C=Label(top,text='DO YOU WANT TO CHECK:',font=('bold',16),anchor=CENTER)
   C.place(x=100,y=0)

   Button(top,text= "Sold Players", command=AUC2020).pack(pady= 5)
   button= Button(top, text="Unsold Players", command=AUCUN2020)
   button.pack(pady=5)

def A19():
   top= Toplevel(root)
   top.geometry("750x500")
   C=Label(top,text='DO YOU WANT TO CHECK:',font=('bold',16),anchor=CENTER)
   C.place(x=100,y=0)

   Button(top,text= "Sold Players", command=AUC2019).pack(pady= 5)
   button= Button(top, text="Unsold Players", command=AUCUN2019)
   button.pack(pady=5)

def POITAB():
   top= Toplevel(root)
   top.geometry("750x500")
   C=Label(top,font=('bold',16),anchor=CENTER)
   C.place(x=100,y=0)

   Button(top,text= "2008").pack(pady= 5)
   Button(top,text= "2009").pack(pady= 5)
   Button(top,text= "2010").pack(pady= 5)
   Button(top,text= "2011").pack(pady= 5)
   Button(top,text= "2012").pack(pady= 5)
   Button(top,text= "2013").pack(pady= 5)
   Button(top,text= "2014").pack(pady= 5)
   Button(top,text= "2015").pack(pady= 5)
   Button(top,text= "2016").pack(pady= 5)
   Button(top,text= "2017").pack(pady= 5)
   Button(top,text= "2018").pack(pady= 5)
   Button(top,text= "2019", command=PT2019).pack(pady= 5)
   Button(top,text= "2020", command=PT2020).pack(pady= 5)
   Button(top,text= "2021", command=PT2021).pack(pady= 5)
   Button(top,text= "2022", command=PT2022).pack(pady= 5)
   Button(top,text= "2023", command=PT2023).pack(pady= 5)



def MOVAPL():
   top= Toplevel(root)
   top.geometry("750x500")
   C=Label(top,font=('bold',16),anchor=CENTER)
   C.place(x=100,y=0)

   Button(top,text= "2008").pack(pady= 5)
   Button(top,text= "2009").pack(pady= 5)
   Button(top,text= "2010").pack(pady= 5)
   Button(top,text= "2011").pack(pady= 5)
   Button(top,text= "2012").pack(pady= 5)
   Button(top,text= "2013").pack(pady= 5)
   Button(top,text= "2014").pack(pady= 5)
   Button(top,text= "2015").pack(pady= 5)
   Button(top,text= "2016").pack(pady= 5)
   Button(top,text= "2017").pack(pady= 5)
   Button(top,text= "2018").pack(pady= 5)
   Button(top,text= "2019", command=MVP1).pack(pady= 5)
   Button(top,text= "2020", command=MVP2).pack(pady= 5)
   Button(top,text= "2021", command=MVP3).pack(pady= 5)
   Button(top,text= "2022").pack(pady= 5)
   Button(top,text= "2023").pack(pady= 5)

def PLASTA():
   top= Toplevel(root)
   top.geometry("750x500")
   C=Label(top,font=('bold',16),anchor=CENTER)
   C.place(x=100,y=0)

   Button(top,text= "2008",command=PP08).pack(pady= 5)
   Button(top,text= "2009").pack(pady= 5)
   Button(top,text= "2010").pack(pady= 5)
   Button(top,text= "2011", command=PP11).pack(pady= 5)
   Button(top,text= "2012").pack(pady= 5)
   Button(top,text= "2013").pack(pady= 5)
   Button(top,text= "2014").pack(pady= 5)
   Button(top,text= "2015").pack(pady= 5)
   Button(top,text= "2016").pack(pady= 5)
   Button(top,text= "2017").pack(pady= 5)
   Button(top,text= "2018").pack(pady= 5)
   Button(top,text= "2019", command=PP19).pack(pady= 5)
   Button(top,text= "2020", command=PP20).pack(pady= 5)
   Button(top,text= "2021", command=PP21).pack(pady= 5)
   Button(top,text= "2022").pack(pady= 5)
   Button(top,text= "2023").pack(pady= 5)

def AUCTION():
   top= Toplevel(root)
   top.geometry("750x500")
   C=Label(top,font=('bold',16),anchor=CENTER)
   C.place(x=100,y=0)

   Button(top,text= "2008").pack(pady= 5)
   Button(top,text= "2009").pack(pady= 5)
   Button(top,text= "2010").pack(pady= 5)
   Button(top,text= "2011").pack(pady= 5)
   Button(top,text= "2012").pack(pady= 5)
   Button(top,text= "2013").pack(pady= 5)
   Button(top,text= "2014").pack(pady= 5)
   Button(top,text= "2015").pack(pady= 5)
   Button(top,text= "2016").pack(pady= 5)
   Button(top,text= "2017").pack(pady= 5)
   Button(top,text= "2018").pack(pady= 5)
   Button(top,text= "2019", command=A19).pack(pady= 5)
   Button(top,text= "2020", command=A20).pack(pady= 5)
   Button(top,text= "2021", command=A21).pack(pady= 5)
   Button(top,text= "2022").pack(pady= 5)
   Button(top,text= "2023").pack(pady= 5)

MVP=Button(root,text='Points Table',font=('bold',30),bg="yellow",command=POITAB)
MVP.place(x=200,y=300)

PT=Button(root,text='MVP(Most Valuable Player)',font=('bold',30),bg="yellow",command=MOVAPL)
PT.place(x=200,y=600)

CS=Button(root,text='Player Stats',font=('bold',30),bg="yellow",command=PLASTA)
CS.place(x=800,y=300)

CSS=Button(root,text='Auction Data',font=('bold',30),bg="yellow",command=AUCTION)
CSS.place(x=800,y=600)


songpl=Button(root,text="Play Music",font=("italic",30),bg="light blue", command=play)
songpl.place(x=1100,y=300)

songpa=Button(root,text="Pause Music",font=("italic",30),bg="light blue", command=pause)
songpa.place(x=1100,y=600)   
    

def close():
      root.destroy()
      pygame.mixer.music.stop()
exit_button = Button(root, text="Exit",bg="red", command=close)
exit_button.pack(pady=10)


i=PIL.Image.open(r"C:\Users\vsais\IPL\LOGO\logo.png")
r=i.resize((350,205),PIL.Image.Resampling.LANCZOS)
s=ImageTk.PhotoImage(r)
img=Label(root, image=s)
img.place(x=600, y=60)
root.mainloop()



