from tkinter import *
import pandas as pd
from tkinter import ttk
import mysql.connector as pro
con=pro.connect(host='localhost',user='root',passwd='VSS@07',database='vss')
def SORT19():
    if con.is_connected()==False:
            print("Error connecting to MySQL database")
    cur=con.cursor()
    cur.execute("select * from mvp2019")
    rows=cur.fetchall()
    l=[]
    pos=[];pla=[];tea=[];mat=[];wick=[];dot=[];four=[];six=[];cat=[];stu=[];rout=[];pts=[]
    for i in rows:
        l+=list(i)
    for i in range(len(l)):
            if i%12==0:
              pos.append(l[i])
              i+=1
              if True:
                  pla.append(l[i])
                  i+=1
                  if True:
                      tea.append(l[i])
                      i+=1
                      if True:
                          mat.append(l[i])
                          i+=1
                          if True:
                              wick.append(l[i])
                              i+=1
                              if True:
                                  dot.append(l[i])
                                  i+=1
                                  if True:
                                      four.append(l[i])
                                      i+=1
                                      if True:
                                          six.append(l[i])
                                          i+=1
                                          if True:
                                              cat.append(l[i])
                                              i+=1
                                              if True:
                                                  stu.append(l[i])
                                                  i+=1
                                                  if True:
                                                      rout.append(l[i])
                                                      i+=1
                                                      if True:
                                                          pts.append(l[i])
                                                          i+=1

    df = pd.DataFrame({"Position":pos,"Player":pla,"Team":tea,"Matches":mat,"Wickets":wick,"Dot Balls":dot,"Fours":four,"Sixes":six,"Catches":cat,"Stumpings":stu,"Run Outs":rout,"Points":pts})
    class app(Tk):
            def __init__(self):
                Tk.__init__(self)
                self.title("MVP")

                self.tree = ttk.Treeview(self)
                columns = list(df.columns)
                self.Combo = ttk.Combobox(self, values=list(df["Team"].unique()),state="readonly")
                self.Combo.pack()
                self.Combo.bind("<<ComboboxSelected>>", self.select_currency)
                self.tree["columns"] = columns
                self.tree.pack(expand=TRUE, fill=BOTH)

                for i in columns:
                    self.tree.column(i, anchor="w")
                    self.tree.heading(i, text=i, anchor="w")

                for index, row in df.iterrows():
                    self.tree.insert("", "end", values=list(row))

            def select_currency(self,event=None):
                self.tree.delete(*self.tree.get_children())
                for index, row in df.loc[df["Team"].eq(self.Combo.get())].iterrows():
                    self.tree.insert("", "end", values=list(row))


                 
    ws = app()
    ws.attributes('-fullscreen', True)
    ws.mainloop()

