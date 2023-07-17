#WAP to accept the inputs and print the NRR(Net Run Rate) of a team(If a team gets all out, the total overs is considered to be 20 overs)
#Tuple having the data form[Runs,wickets,overs,runs,wickets,overs]. 1st half comprises the own
# team and 2nd half for the opponent team
#Format for points table: Position, Team , Matches, Wins, Losses ,Points, NRR
from tkinter import *
from tkinter import ttk
import math
from operator import itemgetter
from tabulate import tabulate
def PT2019():
    CSK=[];MI=[];DC=[];KKR=[];KXIP=[];RCB=[];RR=[];SRH=[]
    CSK.append("Chennai Super Kings")
    MI.append("Mumbai Indians")
    SRH.append("Sunrises Hyderabad")
    KKR.append("Kolkata Knight Riders")
    KXIP.append("Kings XI Punjab")
    RR.append("Rajasthan Royals")
    RCB.append("Royal Challengers Bangalore")
    DC.append("Delhi Capitals")


    M=0;W=0;L=0
    Che=[[71,3,17.4,70,10,17.1],[150,4,19.4,147,6,20],[175,5,20,167,8,20],[133,8,20,170,5,20],[160,3,20,138,5,20],[111,3,17.2,108,9,20],[155,6,20,151,7,20],[162,5,19.4,161,8,20],[132,5,20,137,4,16.5],[160,8,20,161,7,20],[176,4,19.5,175,3,20],[109,10,17.4,155,4,20],[179,4,20,99,10,16.2],[170,5,20,173,4,18]]
    Mum=[[176,10,19.2,213,6,20],[187,8,20,181,5,20],[176,7,20,177,2,18.4],[170,5,20,133,8,20],[136,7,20,96,10,17.4],[198,7,20,197,4,20],[187,5,20,188,6,19.3],[172,5,19,171,7,20],[168,5,20,128,9,20],[161,5,20,162,5,19.1],[155,4,20,109,10,17.4],[198,7,20,232,2,20],[162,5,20,162,6,20],[134,1,16.1,133,7,20]]
    Del=[[213,6,20,176,10,19.2],[147,6,20,150,4,19.4],[185,6,20,185,8,20],[152,10,19.2,166,9,20],[129,8,20,131,5,18.3],[152,6,18.5,149,8,20],[180,3,18.5,178,7,20],[155,7,20,116,10,18.5],[128,9,20,168,5,20],[166,5,19.4,163,7,20],[193,4,19.2,191,6,20],[187,5,20,171,7,20],[99,10,16.2,179,4,20],[121,5,16.1,115,9,20]]
    Kol=[[183,4,19.4,181,3,20],[218,4,20,190,4,20],[185,8,20,185,6,20],[206,5,19.1,205,3,20],[140,2,13.5,139,3,20],[108,9,20,111,3,17.2],[178,7,20,180,3,18.5],[161,8,20,162,5,19.4],[203,5,20,213,4,20],[159,8,20,161,1,15],[175,6,20,177,7,19.2],[232,2,20,198,7,20],[185,3,18,183,6,20],[133,7,20,134,1,16.1]]
    Pun=[[184,4,20,170,9,20],[190,4,20,218,4,20],[177,2,18.4,176,7,20],[166,9,20,152,10,19.2],[138,5,20,160,3,20],[151,4,19.5,150,4,20],[197,4,20,198,7,20],[173,4,20,174,2,19.2],[182,6,20,170,7,20],[163,7,20,166,5,19.4],[185,7,20,202,4,20],[167,8,20,212,6,20],[183,6,20,185,3,18],[173,4,18,170,5,20]]
    Roy=[[70,10,17.1,71,3,17.4],[181,5,20,187,8,20],[113,10,19.5,231,2,20],[158,4,20,164,3,19.5],[205,3,20,206,5,19.1],[149,8,20,152,6,18.5],[174,2,19.2,173,4,20],[171,7,20,172,5,19],[213,4,20,203,5,20],[161,7,20,160,8,20],[202,4,20,185,7,20],[171,7,20,187,5,20],[0,0,0,0,0,0],[178,6,19.2,175,7,20]]
    Raj=[[170,9,20,184,4,20],[198,2,20,201,5,19],[167,8,20,175,5,20],[164,3,19.5,158,4,20],[139,3,20,140,2,13.5],[151,7,20,155,6,20],[188,6,19.3,187,5,20],[170,7,20,182,6,20],[162,5,19.1,161,5,20],[191,6,20,193,4,19.2],[177,7,19.2,175,6,20],[161,3,19.1,160,8,20],[0,0,0,0,0,0],[115,9,20,121,5,16.1]]
    Sun=[[181,3,20,183,4,19.4],[201,5,19,198,2,20],[231,2,20,113,10,19.5],[131,5,18.3,129,8,20],[96,10,17.4,136,7,20],[150,4,20,151,4,19.5],[116,10,18.5,155,7,20],[137,4,16.5,132,5,20],[161,1,15,159,8,20],[175,3,20,176,4,19.5],[160,8,20,161,3,19.1],[212,6,20,167,8,20],[162,6,20,162,5,20],[175,7,20,178,6,19.2]]
    #CSK
    NoR=0
    aa=[];bb=[];cc=[];dd=[];ee=[];ff=[]
    for i in Che:
        if sum(i)>0:
            M+=1
        if i[3]<i[0]:
            W+=1
        if i[3]>i[0]:
            L+=1
        a=i[0];b=i[1];c=i[2];d=i[3];e=i[4];f=i[5]
        aa.append(a)
        bb.append(b)
        cc.append(c)
        dd.append(d)
        ee.append(e)
        ff.append(f)
    A=[]
    for i in range(len(bb)):
       if bb[i] == 10:
          A.append(i)
          cc[i]=20
    B=[]
    for i in range(len(ee)):
       if ee[i] == 10:
          B.append(i)
          ff[i]=20
    nl=[];nm=[]
    g=sum(aa)
    h=sum(dd)
    for i in cc:
         TOTY= int(int(i)*6+round((i-int(i))*10,0))
         nm.append(TOTY)
    for i in ff:
         TOTO=int(int(i)*6+round ((i-int(i))*10,0))
         nl.append(TOTO)
    nn=sum(nm)/6
    no=sum(nl)/6
    NRR=round((g/nn)-(h/no),3)
    P=W*2
    sup=0
    wi=0;l=0
    W+=wi
    L+=l
    Ext=(wi*2)+P
    M+=NoR
    Ext+=NoR
    CSK.append(M)
    CSK.append(W)
    CSK.append(L)
    CSK.append(NoR)
    CSK.append(NRR)
    CSK.append(Ext)


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
    sup=1
    wi=1;l=0
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
    sup=1
    wi=1;l=0
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
    sup=1
    wi=0;l=1
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
    NoR=1
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


    #RR
    NoR=1
    gg=[];hh=[];ii=[];jj=[];kk=[];ll=[];M=0;W=0;L=0;NRR=0
    for i in Raj:
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
    RR.append(M)
    RR.append(W)
    RR.append(L)
    RR.append(NoR)
    RR.append(NRR)
    RR.append(Ext)


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
    sup=1
    wi=0;l=1
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





    OVR=[]
    OVR.append(CSK)
    OVR.append(DC)
    OVR.append(KKR)
    OVR.append(MI)
    OVR.append(KXIP)
    OVR.append(RCB)
    OVR.append(RR)
    OVR.append(SRH)

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

    
    

