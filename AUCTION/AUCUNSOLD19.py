from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector as pro

def AUCUN2019():
    def update(rows):
            tree.delete(*tree.get_children())
            for i in rows:
                tree.insert('','end',values=i)

    def default():
            ab=Ent.get()
            cur.execute("SELECT * from aucunsold2019")
            rows=cur.fetchall()
            update(rows)

    def bowl():
            ab=Ent.get()
            cur.execute("SELECT * from aucunsold2019 where Player LIKE '%"+ab+"%' and Type LIKE '%Bowl%' ")
            rows=cur.fetchall()
            update(rows)

    def bat():
            ab=Ent.get()
            cur.execute("SELECT * from aucunsold2019 where Player LIKE '%"+ab+"%' and Type LIKE '%Bat%' ")
            rows=cur.fetchall()
            update(rows)

    def allr():
            ab=Ent.get()
            cur.execute("SELECT * from aucunsold2019 where Player LIKE '%"+ab+"%' and Type LIKE '%All%'")
            rows=cur.fetchall()
            update(rows)

    def wk():
            ab=Ent.get()
            cur.execute("SELECT * from aucunsold2019 where Player LIKE '%"+ab+"%' and Type LIKE '%Keep%'")
            rows=cur.fetchall()
            update(rows)

    def price():
            ab=Ent.get()
            cur.execute("SELECT * from aucunsold2019 where Player LIKE '%"+ab+"%' order by length(Price) desc,Price desc")
            rows=cur.fetchall()
            update(rows)
    

    def player():
            ab=Ent.get()
            cur.execute("SELECT * from aucunsold2019 where Player LIKE '%"+ab+"%'")
            player1()

    def player1():
            rows=cur.fetchall()
            c=cur.rowcount
            if c==1:
                k=0
                co=[["Player","Type","Base Price"]]
                op=Tk()
                w=LabelFrame(op,text="Single player stats")
                w.pack(fill="both",expand="yes",padx=20,pady=10)
                ree = ttk.Treeview(w, column=("Attributes","Stats"), show='headings', height=3)
                ree.pack()
                ree.column("# 1", anchor=CENTER)
                ree.heading("# 1", text="Attributes")
                ree.column("# 2", anchor=CENTER)
                ree.heading("# 2", text="Stats")
                for i in rows:
                    while k<=2:
                        co.append(i)
                        co[1]=list(co[1])
                        ree.insert('','end',values=(co[0][k],co[1][k]))
                        k+=1
                def close():
                    op.destroy()
                exit_button = Button(op, text="Exit", command=close)
                exit_button.pack(pady=20) 
            else:
                update(rows)


    
    con=pro.connect(host='localhost',user='root',passwd='VSS@07',database='ipl')
    cur=con.cursor()

    ws=Tk()
    b=StringVar()
    ws.geometry("700x350")
    style = ttk.Style()
    style.theme_use('clam')



    w1=LabelFrame(ws,text="Unsold Players")
    w2=LabelFrame(ws,text="Search Player")
    
    w1.pack(fill="both",expand="yes",padx=20,pady=10)
    w2.pack(fill="both",expand="yes",padx=20,pady=10)

    

    tree = ttk.Treeview(w1, column=("Player","Type","Base Price"), show='headings', height=30)
    tree.pack()
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Player")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Type")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="Base Price")


            

    cur=con.cursor()
    cur.execute("select * from aucunsold2019")
    rows=cur.fetchall()
    update(rows)


    Lab=Label(w2,text="Search")
    Lab.pack(side=tk.LEFT,padx=10)
    Ent=Entry(w2,textvariable=b)
    Ent.pack(side=tk.LEFT,padx=6)
    bt=Button(w2,text="Search Player",command=player)
    bt.pack(side=tk.LEFT,padx=6)
    bt=Button(w2,text="Default",command=default)
    bt.pack(side=tk.LEFT,padx=10)
    bt=Button(w2,text="Sort by Bowlers",command=bowl)
    bt.pack(side=tk.LEFT,padx=6)
    bt=Button(w2,text="Sort by Batsmen",command=bat)
    bt.pack(side=tk.LEFT,padx=6)
    bt=Button(w2,text="Sort by All-Rounders",command=allr)
    bt.pack(side=tk.LEFT,padx=6)
    bt=Button(w2,text="Sort by Wicket Keepers",command=wk)
    bt.pack(side=tk.LEFT,padx=6)
    bt=Button(w2,text="Sort by Base Price",command=price)
    bt.pack(side=tk.LEFT,padx=6)



    



    ws.attributes('-fullscreen', True)
    def close():
      ws.destroy()

    exit_button = Button(ws, text="Exit", command=close)
    exit_button.pack(pady=20)
    ws.mainloop()

