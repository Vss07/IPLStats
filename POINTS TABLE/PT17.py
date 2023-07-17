#WAP to accept the inputs and print the NRR(Net Run Rate) of a team(If a team gets all out, the total overs is considered to be 20 overs)
#Tuple having the data form[Runs,wickets,overs,runs,wickets,overs]. 1st half comprises the own
# team and 2nd half for the opponent team
#Format for points table: Position, Team , Matches, Wins, Losses ,Points, NRR
from tkinter import *
from tkinter import ttk
import math
from operator import itemgetter
from tabulate import tabulate
def PT2017():
    MI=[];DC=[];KKR=[];KXIP=[];RCB=[];SRH=[];RPS=[];GT=[]
    MI.append("Mumbai Indians")
    SRH.append("Sunrises Hyderabad")
    KKR.append("Kolkata Knight Riders")
    KXIP.append("Kings XI Punjab")
    RCB.append("Royal Challengers Bangalore")
    DC.append("Delhi Capitals")
    RPS.append("Rising Pune Supergiants")
    GL.append("Gujarat Lions")

    M=0;W=0;L=0
    Mum=[[184,8,20,187,3,19.5],[180]]
    Del=[[]]
    Kol=[[]]
    Pun=[[]]
    Roy=[[]]
    Sun=[[]]
    Pun=[[]]
    Guj=[[]]
    
    #MI
    NoR=0
    gg=[];hh=[];ii=[];jj=[];kk=[];ll=[];M=0;W=0;L=0;NRR=0
    for i in Mum:
        if sum(i)>0:
            M+=1
        if i[3]<i[0]:
            W+=1
        if i[3]>i[0]:
            L+=1
        g=i[0];h=i[1];ik=i[2];k=i[3];l=i[4];m=i[5]
        gg.append(g)
        hh.append(h)
        ii.append(ik)
        jj.append(k)
        kk.append(l)
        ll.append(m)
    O=[]
    for i in range(len(hh)):
       if hh[i] == 10:
          O.append(i)
          ii[i]=20
    I=[]
    for i in range(len(kk)):
       if kk[i] == 10:
          I.append(i)
          ll[i]=20
    np=[];nq=[]
    gh=sum(gg)
    hg=sum(jj)
    for i in ii:
         TOTX= int(int(i)*6+round((i-int(i))*10,0))
         np.append(TOTX)
    for i in ll:
         TOTN=int(int(i)*6+round ((i-int(i))*10,0))
         nq.append(TOTN)
    nr=sum(np)/6
    ns=sum(nq)/6
    NRR=round((gh/nr)-(hg/ns),3)
    P=W*2
    sup=0
    wi=0;l=0
    Ext=(wi*2)+P
    W+=wi
    L+=l
    M+=NoR
    Ext+=NoR
    MI.append(M)
    MI.append(W)
    MI.append(L)
    MI.append(NoR)
    MI.append(NRR)
    MI.append(Ext)

    #DC
    NoR=0
    mm=[];nn=[];oo=[];pp=[];qq=[];rr=[];M=0;W=0;L=0;NRR=0
    for i in Del:
        if sum(i)>0:
            M+=1
        if i[3]<i[0]:
            W+=1
        if i[3]>i[0]:
            L+=1
        g=i[0];h=i[1];ik=i[2];k=i[3];l=i[4];m=i[5]
        mm.append(g)
        nn.append(h)
        oo.append(ik)
        pp.append(k)
        qq.append(l)
        rr.append(m)
    O=[]
    for i in range(len(nn)):
       if nn[i] == 10:
          O.append(i)
          oo[i]=20
    I=[]
    for i in range(len(qq)):
       if qq[i] == 10:
          I.append(i)
          rr[i]=20
    np=[];nq=[]
    gh=sum(mm)
    hg=sum(pp)
    for i in oo:
         TOTX= int(int(i)*6+round((i-int(i))*10,0))
         np.append(TOTX)
    for i in rr:
         TOTN=int(int(i)*6+round ((i-int(i))*10,0))
         nq.append(TOTN)
    nr=sum(np)/6
    ns=sum(nq)/6
    NRR=round((gh/nr)-(hg/ns),3)
    P=W*2
    sup=0
    wi=0;l=0
    L+=l
    W+=wi
    Ext=(wi*2)+P
    M+=NoR
    Ext+=NoR
    DC.append(M)
    DC.append(W)
    DC.append(L)
    DC.append(NoR)
    DC.append(NRR)
    DC.append(Ext)
    NR=0
    #KKR
    NoR=0
    gg=[];hh=[];ii=[];jj=[];kk=[];ll=[];M=0;W=0;L=0;NRR=0
    for i in Kol:
        if sum(i)>0:
            M+=1
        if i[3]<i[0]:
            W+=1
        if i[3]>i[0]:
            L+=1
        g=i[0];h=i[1];ik=i[2];k=i[3];l=i[4];m=i[5]
        gg.append(g)
        hh.append(h)
        ii.append(ik)
        jj.append(k)
        kk.append(l)
        ll.append(m)
    O=[]
    for i in range(len(hh)):
       if hh[i] == 10:
          O.append(i)
          ii[i]=20
    I=[]
    for i in range(len(kk)):
       if kk[i] == 10:
          I.append(i)
          ll[i]=20
    np=[];nq=[]
    gh=sum(gg)
    hg=sum(jj)
    for i in ii:
         TOTX= int(int(i)*6+round((i-int(i))*10,0))
         np.append(TOTX)
    for i in ll:
         TOTN=int(int(i)*6+round ((i-int(i))*10,0))
         nq.append(TOTN)
    nr=sum(np)/6
    ns=sum(nq)/6
    NRR=round((gh/nr)-(hg/ns),3)
    P=W*2
    sup=0
    wi=0;l=0
    L+=l
    W+=wi
    Ext=(wi*2)+P
    M+=NoR
    Ext+=NoR
    KKR.append(M)
    KKR.append(W)
    KKR.append(L)
    KKR.append(NoR)
    KKR.append(NRR)
    KKR.append(Ext)

    #KXIP
    NoR=0
    gg=[];hh=[];ii=[];jj=[];kk=[];ll=[];M=0;W=0;L=0;NRR=0
    for i in Pun:
        if sum(i)>0:
            M+=1
        if i[3]<i[0]:
            W+=1
        if i[3]>i[0]:
            L+=1
        g=i[0];h=i[1];ik=i[2];k=i[3];l=i[4];m=i[5]
        gg.append(g)
        hh.append(h)
        ii.append(ik)
        jj.append(k)
        kk.append(l)
        ll.append(m)
    O=[]
    for i in range(len(hh)):
       if hh[i] == 10:
          O.append(i)
          ii[i]=20
    I=[]
    for i in range(len(kk)):
       if kk[i] == 10:
          I.append(i)
          ll[i]=20
    np=[];nq=[]
    gh=sum(gg)
    hg=sum(jj)
    for i in ii:
         TOTX= int(int(i)*6+round((i-int(i))*10,0))
         np.append(TOTX)
    for i in ll:
         TOTN=int(int(i)*6+round ((i-int(i))*10,0))
         nq.append(TOTN)
    nr=sum(np)/6
    ns=sum(nq)/6
    NRR=round((gh/nr)-(hg/ns),3)
    P=W*2
    sup=0;l=0
    L+=l
    wi=0
    W+=wi
    Ext=(wi*2)+P
    M+=NoR
    Ext+=NoR
    KXIP.append(M)
    KXIP.append(W)
    KXIP.append(L)
    KXIP.append(NoR)
    KXIP.append(NRR)
    KXIP.append(Ext)

    #RCB
    NoR=0
    gg=[];hh=[];ii=[];jj=[];kk=[];ll=[];M=0;W=0;L=0;NRR=0
    for i in Roy:
        if sum(i)>0:
            M+=1
        if i[3]<i[0]:
            W+=1
        if i[3]>i[0]:
            L+=1
        g=i[0];h=i[1];ik=i[2];k=i[3];l=i[4];m=i[5]
        gg.append(g)
        hh.append(h)
        ii.append(ik)
        jj.append(k)
        kk.append(l)
        ll.append(m)
    O=[]
    for i in range(len(hh)):
       if hh[i] == 10:
          O.append(i)
          ii[i]=20
    I=[]
    for i in range(len(kk)):
       if kk[i] == 10:
          I.append(i)
          ll[i]=20
    np=[];nq=[]
    gh=sum(gg)
    hg=sum(jj)
    for i in ii:
         TOTX= int(int(i)*6+round((i-int(i))*10,0))
         np.append(TOTX)
    for i in ll:
         TOTN=int(int(i)*6+round ((i-int(i))*10,0))
         nq.append(TOTN)
    nr=sum(np)/6
    ns=sum(nq)/6
    NRR=round((gh/nr)-(hg/ns),3)
    P=W*2
    sup=0
    wi=0;l=0
    L+=l
    W+=wi
    Ext=(wi*2)+P
    M+=NoR
    Ext+=NoR
    RCB.append(M)
    RCB.append(W)
    RCB.append(L)
    RCB.append(NoR)
    RCB.append(NRR)
    RCB.append(Ext)


    
    #SRH
    NoR=0
    gg=[];hh=[];ii=[];jj=[];kk=[];ll=[];M=0;W=0;L=0;NRR=0
    for i in Sun:
        if sum(i)>0:
            M+=1
        if i[3]<i[0]:
            W+=1
        if i[3]>i[0]:
            L+=1
        g=i[0];h=i[1];ik=i[2];k=i[3];l=i[4];m=i[5]
        gg.append(g)
        hh.append(h)
        ii.append(ik)
        jj.append(k)
        kk.append(l)
        ll.append(m)
    O=[]
    for i in range(len(hh)):
       if hh[i] == 10:
          O.append(i)
          ii[i]=20
    I=[]
    for i in range(len(kk)):
       if kk[i] == 10:
          I.append(i)
          ll[i]=20
    np=[];nq=[]
    gh=sum(gg)
    hg=sum(jj)
    for i in ii:
         TOTX= int(int(i)*6+round((i-int(i))*10,0))
         np.append(TOTX)
    for i in ll:
         TOTN=int(int(i)*6+round ((i-int(i))*10,0))
         nq.append(TOTN)
    nr=sum(np)/6
    ns=sum(nq)/6
    NRR=round((gh/nr)-(hg/ns),3)
    P=W*2
    sup=0
    wi=0;l=0
    L+=l
    W+=wi
    Ext=(wi*2)+P
    M+=NoR
    Ext+=NoR
    SRH.append(M)
    SRH.append(W)
    SRH.append(L)
    SRH.append(NoR)
    SRH.append(NRR)
    SRH.append(Ext)

    #RPS
    NoR=0
    gg=[];hh=[];ii=[];jj=[];kk=[];ll=[];M=0;W=0;L=0;NRR=0
    for i in Pun:
        if sum(i)>0:
            M+=1
        if i[3]<i[0]:
            W+=1
        if i[3]>i[0]:
            L+=1
        g=i[0];h=i[1];ik=i[2];k=i[3];l=i[4];m=i[5]
        gg.append(g)
        hh.append(h)
        ii.append(ik)
        jj.append(k)
        kk.append(l)
        ll.append(m)
    O=[]
    for i in range(len(hh)):
       if hh[i] == 10:
          O.append(i)
          ii[i]=20
    I=[]
    for i in range(len(kk)):
       if kk[i] == 10:
          I.append(i)
          ll[i]=20
    np=[];nq=[]
    gh=sum(gg)
    hg=sum(jj)
    for i in ii:
         TOTX= int(int(i)*6+round((i-int(i))*10,0))
         np.append(TOTX)
    for i in ll:
         TOTN=int(int(i)*6+round ((i-int(i))*10,0))
         nq.append(TOTN)
    nr=sum(np)/6
    ns=sum(nq)/6
    NRR=round((gh/nr)-(hg/ns),3)
    P=W*2
    sup=0
    wi=0;l=0
    L+=l
    W+=wi
    Ext=(wi*2)+P
    M+=NoR
    Ext+=NoR
    RPS.append(M)
    RPS.append(W)
    RPS.append(L)
    RPS.append(NoR)
    RPS.append(NRR)
    RPS.append(Ext)

    #GL
    NoR=0
    gg=[];hh=[];ii=[];jj=[];kk=[];ll=[];M=0;W=0;L=0;NRR=0
    for i in Guj:
        if sum(i)>0:
            M+=1
        if i[3]<i[0]:
            W+=1
        if i[3]>i[0]:
            L+=1
        g=i[0];h=i[1];ik=i[2];k=i[3];l=i[4];m=i[5]
        gg.append(g)
        hh.append(h)
        ii.append(ik)
        jj.append(k)
        kk.append(l)
        ll.append(m)
    O=[]
    for i in range(len(hh)):
       if hh[i] == 10:
          O.append(i)
          ii[i]=20
    I=[]
    for i in range(len(kk)):
       if kk[i] == 10:
          I.append(i)
          ll[i]=20
    np=[];nq=[]
    gh=sum(gg)
    hg=sum(jj)
    for i in ii:
         TOTX= int(int(i)*6+round((i-int(i))*10,0))
         np.append(TOTX)
    for i in ll:
         TOTN=int(int(i)*6+round ((i-int(i))*10,0))
         nq.append(TOTN)
    nr=sum(np)/6
    ns=sum(nq)/6
    NRR=round((gh/nr)-(hg/ns),3)
    P=W*2
    sup=0
    wi=0;l=0
    L+=l
    W+=wi
    Ext=(wi*2)+P
    M+=NoR
    Ext+=NoR
    GL.append(M)
    GL.append(W)
    GL.append(L)
    GL.append(NoR)
    GL.append(NRR)
    GL.append(Ext)



    OVR=[]
    OVR.append(DC)
    OVR.append(KKR)
    OVR.append(MI)
    OVR.append(KXIP)
    OVR.append(RCB)
    OVR.append(SRH)
    OVR.append(RPS)
    OVR.append(GL)

    abc=sorted(OVR, key=itemgetter(6,5),reverse=True)
    Pos=[1,2,3,4,5,6,7,8]
    for i in range(1,9):
        abc[i-1].insert(0,i)


    win = Tk()
    win.geometry("700x350")

    colu=["Position", "Team", "Matches","Wins","Losses","No Result","Net Run Rate","Points"]
    tree = ttk.Treeview(win, column=("Position", "Team", "Matches","Wins","Losses","No Result","Net Run Rate","Points"), show='headings', height=8)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Position")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Team")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="Matches")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="Wins")
    tree.column("# 5", anchor=CENTER)
    tree.heading("# 5", text="Losses")
    tree.column("# 6", anchor=CENTER)
    tree.heading("# 6", text="No Result")
    tree.column("# 7", anchor=CENTER)
    tree.heading("# 7", text="Net Run Rate")
    tree.column("# 8", anchor=CENTER)
    tree.heading("# 8", text="Points")

    def close():
       win.destroy()

    exit_button = Button(win, text="Exit", command=close)
    exit_button.pack(pady=20)

    tree.insert('', 'end', text="1", values=(abc[0][0], abc[0][1],abc[0][2],abc[0][3],abc[0][4],abc[0][5],abc[0][6],abc[0][7] ))
    tree.insert('', 'end', text="1", values=(abc[1][0], abc[1][1],abc[1][2],abc[1][3],abc[1][4],abc[1][5],abc[1][6],abc[1][7] ))
    tree.insert('', 'end', text="1", values=(abc[2][0], abc[2][1],abc[2][2],abc[2][3],abc[2][4],abc[2][5],abc[2][6],abc[2][7] ))
    tree.insert('', 'end', text="1", values=(abc[3][0], abc[3][1],abc[3][2],abc[3][3],abc[3][4],abc[3][5],abc[3][6],abc[3][7] ))
    tree.insert('', 'end', text="1", values=(abc[4][0], abc[4][1],abc[4][2],abc[4][3],abc[4][4],abc[4][5],abc[4][6],abc[4][7] ))
    tree.insert('', 'end', text="1", values=(abc[5][0], abc[5][1],abc[5][2],abc[5][3],abc[5][4],abc[5][5],abc[5][6],abc[5][7] ))
    tree.insert('', 'end', text="1", values=(abc[6][0], abc[6][1],abc[6][2],abc[6][3],abc[6][4],abc[6][5],abc[6][6],abc[6][7] ))
    tree.insert('', 'end', text="1", values=(abc[7][0], abc[7][1],abc[7][2],abc[7][3],abc[7][4],abc[7][5],abc[7][6],abc[7][7] ))
 
    tree.pack()

    win.mainloop()

    
    

