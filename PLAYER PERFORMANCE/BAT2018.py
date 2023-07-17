from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector as pro
e=''
def BT2018():
    def update(rows):
            tree.delete(*tree.get_children())
            for i in rows:
                tree.insert('','end',values=i)

    def default():
            global e
            e=''
            ab=Ent.get()
            cur.execute("SELECT * from batting2018")
            rows=cur.fetchall()
            update(rows)

    def centuries():
            ab=Ent.get()
            cur.execute("SELECT * from batting2018 where Player LIKE '%"+ab+"%' and Team LIKE '%"+e+"%' Order by Centuries DESC")
            rows=cur.fetchall()
            update(rows)

    def fifties():
            ab=Ent.get()
            cur.execute("SELECT * from batting2018 where Player LIKE '%"+ab+"%' and Team LIKE '%"+e+"%' Order by Fifties DESC")
            rows=cur.fetchall()
            update(rows)

    def strate():
            ab=Ent.get()
            cur.execute("SELECT * from batting2018 where Player LIKE '%"+ab+"%' and Team LIKE '%"+e+"%' Order by StrikeRate DESC")
            rows=cur.fetchall()
            update(rows)

    def avg():
            ab=Ent.get()
            cur.execute("SELECT * from batting2018 where Player LIKE '%"+ab+"%' and Team LIKE '%"+e+"%' Order by Average DESC")
            rows=cur.fetchall()
            update(rows)
    

    def player():
            ab=Ent.get()
            cur.execute("SELECT * from batting2018 where Player LIKE '%"+ab+"%'")
            player1()

    def player1():
            rows=cur.fetchall()
            c=cur.rowcount
            if c==1:
                k=0
                co=[["Position", "Player","Team","Matches","Innings","Not Outs","Runs","Balls Faced","Centuries","Fifties","Strike Rate","Average"]]
                op=Tk()
                w=LabelFrame(op,text="Single player stats")
                w.pack(fill="both",expand="yes",padx=20,pady=10)
                ree = ttk.Treeview(w, column=("Attributes","Stats"), show='headings', height=12)
                ree.pack()
                ree.column("# 1", anchor=CENTER)
                ree.heading("# 1", text="Attributes")
                ree.column("# 2", anchor=CENTER)
                ree.heading("# 2", text="Stats")
                for i in rows:
                    while k<=11:
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

    def CSK():
            global e
            e='Chennai Super Kings'
            ab=Ent.get()
            cur.execute("SELECT * from batting2018 where Team LIKE '%Chennai%' and Player LIKE '%"+ab+"%'")
            rows=cur.fetchall()
            update(rows)

    def MI():
            global e
            e='Mumbai Indians'
            ab=Ent.get()
            cur.execute("SELECT * from batting2018 where Team LIKE '%Mumbai%'and Player LIKE '%"+ab+"%'")
            rows=cur.fetchall()
            update(rows)

    def DC():
            global e
            e='Delhi Capitals'
            ab=Ent.get()
            cur.execute("SELECT * from batting2018 where Team LIKE '%Delhi%' and Player LIKE '%"+ab+"%'")
            rows=cur.fetchall()
            update(rows)

    def KKR():
            global e
            e='Kolkata Knight Riders'
            ab=Ent.get()
            cur.execute("SELECT * from batting2018 where Team LIKE '%Kolkata%' and Player LIKE '%"+ab+"%'")
            rows=cur.fetchall()
            update(rows)

    def KXIP():
            global e
            e='Kings XI Punjab'
            ab=Ent.get()
            cur.execute("SELECT * from batting2018 where Team LIKE '%Punjab%' and Player LIKE '%"+ab+"%'")
            rows=cur.fetchall()
            update(rows)

    def RR():
            global e
            e='Rajasthan Royals'
            ab=Ent.get()
            cur.execute("SELECT * from batting2018 where Team LIKE '%Rajasthan%' and Player LIKE '%"+ab+"%'")
            rows=cur.fetchall()
            update(rows)

    def RCB():
            global e
            e='Royal Challengers Bangalore'
            ab=Ent.get()
            cur.execute("SELECT * from batting2018 where Team LIKE '%Bangalore%' and Player LIKE '%"+ab+"%'")
            rows=cur.fetchall()
            update(rows)

    def SRH():
            global e
            e='Deccan Chargers'
            ab=Ent.get()
            cur.execute("SELECT * from batting2018 where Team LIKE '%Hyderabad%' and Player LIKE '%"+ab+"%'")
            rows=cur.fetchall()
            update(rows)

    
    con=pro.connect(host='localhost',user='root',passwd='VSS@07',database='ipl')
    cur=con.cursor()

    ws=Tk()
    b=StringVar()
    ws.geometry("700x350")
    style = ttk.Style()
    style.theme_use('clam')



    w1=LabelFrame(ws,text="Batting Stats")
    w2=LabelFrame(ws,text="Search Player")
    w3=LabelFrame(ws,text="Sort Player")


    w1.pack(fill="both",expand="yes",padx=20,pady=10)
    w2.pack(fill="both",expand="yes",padx=20,pady=10)
    w3.pack(fill="both",expand="yes",padx=20,pady=10)


    

    tree = ttk.Treeview(w1, column=( "Position", "Player","Team","Matches","Innings","Not Outs","Runs","Balls Faced","Centuries","Fifties","Strike Rate","Average"), show='headings', height=30)
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
    tree.heading("# 5", text="Innings")
    tree.column("# 6", anchor=CENTER)
    tree.heading("# 6", text="Not Outs")
    tree.column("# 7", anchor=CENTER)
    tree.heading("# 7", text="Runs")
    tree.column("# 8", anchor=CENTER)
    tree.heading("# 8", text="Balls Faced")
    tree.column("# 9", anchor=CENTER)
    tree.heading("# 9", text="Centuries")
    tree.column("# 10", anchor=CENTER)
    tree.heading("# 10", text="Fifties")
    tree.column("# 11", anchor=CENTER)
    tree.heading("# 11", text="Strike Rate")
    tree.column("# 12", anchor=CENTER)
    tree.heading("# 12", text="Average")

            

    cur=con.cursor()
    cur.execute("select * from batting2018")
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
    bt=Button(w2,text="Sort by Centuries",command=centuries)
    bt.pack(side=tk.LEFT,padx=6)
    bt=Button(w2,text="Sort by Fifties",command=fifties)
    bt.pack(side=tk.LEFT,padx=6)
    bt=Button(w2,text="Sort by Strike Rate",command=strate)
    bt.pack(side=tk.LEFT,padx=6)
    bt=Button(w2,text="Sort by Average",command=avg)
    bt.pack(side=tk.LEFT,padx=6)

    
    but=Button(w3,text="Default",command=default)
    but.pack(side=tk.LEFT,padx=6)
    but=Button(w3,text="Chennai Super Kings",command=CSK)
    but.pack(side=tk.LEFT,padx=6)
    but=Button(w3,text="Mumbai Indians",command=MI)
    but.pack(side=tk.LEFT,padx=6)
    but=Button(w3,text="Delhi Capitals",command=DC)
    but.pack(side=tk.LEFT,padx=6)
    but=Button(w3,text="Kolkata Knight Riders",command=KKR)
    but.pack(side=tk.LEFT,padx=6)
    but=Button(w3,text="Kings XI Punjab",command=KXIP)
    but.pack(side=tk.LEFT,padx=6)
    but=Button(w3,text="Rajasthan Royals",command=RR)
    but.pack(side=tk.LEFT,padx=6)
    but=Button(w3,text="Royal Challengers Bangalore",command=RCB)
    but.pack(side=tk.LEFT,padx=6)
    but=Button(w3,text="Sunrisers Hyderabad",command=SRH)
    but.pack(side=tk.LEFT,padx=6)

    
    

    



    ws.attributes('-fullscreen', True)
    def close():
      ws.destroy()

    exit_button = Button(ws, text="Exit", command=close)
    exit_button.pack(pady=20)
    ws.mainloop()
