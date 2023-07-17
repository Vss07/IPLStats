from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector as pro
def sea20():
    def update(rows):
            tree.delete(*tree.get_children())
            for i in rows:
                tree.insert('','end',values=i)

    def search():
            ab=Ent.get()
            cur.execute("SELECT * from mvp2020 where Player LIKE '%"+ab+"%'")
            rows=cur.fetchall()
            update(rows)

    con=pro.connect(host='localhost',user='root',passwd='VSS@07',database='vss')
    cur=con.cursor()

    ws=Tk()
    b=StringVar()
    ws.geometry("700x350")
    style = ttk.Style()
    style.theme_use('clam')



    w1=LabelFrame(ws,text="Most Valuble Player")
    w2=LabelFrame(ws,text="Search by Player")

    w1.pack(fill="both",expand="yes",padx=20,pady=10)
    w2.pack(fill="both",expand="yes",padx=20,pady=10)

    

    tree = ttk.Treeview(w1, column=( "Position", "Player","Team","Matches","Wickets","Dot Balls","Fours","Sixes","Catches","Stumpings","Run Outs","Points"), show='headings', height=30)
    tree.pack()
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Position")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Player")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="Team")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="Matches")
    tree.column("# 5", anchor=CENTER)
    tree.heading("# 5", text="Wickets")
    tree.column("# 6", anchor=CENTER)
    tree.heading("# 6", text="Dot Balls")
    tree.column("# 7", anchor=CENTER)
    tree.heading("# 7", text="Fours")
    tree.column("# 8", anchor=CENTER)
    tree.heading("# 8", text="Sixes")
    tree.column("# 9", anchor=CENTER)
    tree.heading("# 9", text="Catches")
    tree.column("# 10", anchor=CENTER)
    tree.heading("# 10", text="Stumpings")
    tree.column("# 11", anchor=CENTER)
    tree.heading("# 11", text="Run Outs")
    tree.column("# 12", anchor=CENTER)
    tree.heading("# 12", text="Points")

            

    cur=con.cursor()
    cur.execute("select * from mvp2020")
    rows=cur.fetchall()
    update(rows)


    Lab=Label(w2,text="Search")
    Lab.pack(side=tk.LEFT,padx=10)
    Ent=Entry(w2,textvariable=b)
    Ent.pack(side=tk.LEFT,padx=6)
    bt=Button(w2,text="Search",command=search)
    bt.pack(side=tk.LEFT,padx=6)




    ws.attributes('-fullscreen', True)
    ws.mainloop()
