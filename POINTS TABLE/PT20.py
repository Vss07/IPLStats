#WAP to accept the inputs and print the NRR(Net Run Rate) of a team(If a team gets all out, the total overs is considered to be 20 overs)
#Tuple having the data form[Runs,wickets,overs,runs,wickets,overs]. 1st half comprises the own
# team and 2nd half for the opponent team
#Format for points table: Position, Team , Matches, Wins, Losses ,Points, NRR
import math
from operator import itemgetter
from tabulate import tabulate
from tkinter import *
from tkinter import ttk
def PT2020():
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
    Che=[[166,5,19.2,162,9,20],[200,6,20,216,7,20],[131,7,20,175,3,20],[157,5,20,164,5,20],[181,0,17.4,178,4,20],[157,5,20,167,10,10],[132,8,20,169,4,20],[167,6,20,147,8,20],[179,4,20,185,5,19.5],[125,5,20,126,3,17.3],[114,9,20,116,0,12.2],[150,2,18.4,145,6,20],[178,4,20,172,5,20],[154,1,18.5,153,6,20]]
    Mum=[[162,9,20,166,5,19.2],[195,5,20,146,9,20],[201,5,20,201,3,20],[191,4,20,143,8,20],[208,5,20,174,7,20],[193,4,20,136,10,18.1],[166,5,19.4,162,4,20],[149,2,16.5,148,5,20],[176,6,20,176,6,20],[116,0,12.2,114,9,20],[195,5,20,196,2,18.2],[166,5,19.1,164,6,20],[111,1,14.2,110,9,20],[149,8,20,151,0,17.1]]
    Del=[[157,8,20,157,8,20],[175,3,20,131,7,20],[147,7,20,162,4,20],[228,4,20,210,8,20],[196,4,20,137,9,20],[184,8,20,138,10,19.4],[162,4,20,166,5,19.4],[161,7,20,148,8,20],[185,5,19.5,179,4,20],[164,5,20,167,5,19],[135,9,20,194,6,20],[131,10,19,219,2,20],[110,9,20,111,1,14.2],[154,4,19,152,7,20]]
    Kol=[[146,9,20,195,5,20],[145,3,18,142,4,20],[174,6,20,137,9,20],[210,8,20,228,4,20],[167,10,20,157,5,20],[164,6,20,162,5,20],[112,9,20,194,2,20],[148,5,20,149,2,16.5],[163,5,20,163,6,20],[84,8,20,85,2,13.3],[194,6,20,135,9,20],[149,9,20,150,2,18.5],[172,5,20,178,4,20],[191,7,20,131,9,20]]
    Pun=[[157,8,20,157,8,20],[206,3,20,109,10,17],[223,2,20,226,6,19.3],[143,8,20,191,4,20],[178,4,20,181,0,17.4],[132,10,16.5,201,6,20],[162,5,20,164,6,20],[177,2,20,171,6,20],[176,6,20,176,6,20],[167,5,19,164,5,20],[126,7,20,114,10,19.5],[150,2,18.5,149,9,20],[185,4,20,186,3,17.3],[153,6,20,154,1,18.5]]
    Roy=[[163,5,20,153,10,19.4],[109,10,17,206,3,20],[201,3,20,201,5,20],[158,2,19.1,154,6,20],[137,9,20,196,4,20],[169,4,20,132,8,20],[194,2,20,112,9,20],[171,6,20,177,2,20],[179,3,19.4,177,6,20],[85,2,13.3,84,8,20],[145,6,20,150,2,18.4],[164,6,20,166,5,19.1],[120,7,20,121,5,14.1],[152,7,20,154,4,19]]
    Raj=[[216,7,20,200,6,20],[226,6,19.3,223,2,20],[137,9,20,174,6,20],[154,6,20,158,2,19.1],[136,10,18.1,193,4,20],[138,10,19.4,184,8,20],[163,5,19.5,158,4,20],[148,8,20,161,7,20],[177,6,20,179,3,19.4],[126,3,17.3,125,5,20],[154,6,20,156,2,18.1],[196,2,18.2,195,5,20],[186,3,17.3,185,4,20],[131,9,20,191,7,20]]
    Sun=[[153,10,19.4,163,5,20],[142,4,20,145,3,18],[162,4,20,147,7,20],[164,5,20,157,5,20],[174,7,20,208,5,20],[201,6,20,132,10,16.5],[158,4,20,163,5,19.5],[147,8,20,167,6,20],[163,6,20,163,5,20],[156,2,18.1,154,6,20],[114,10,19.5,126,7,20],[219,2,20,131,10,19],[121,5,14.1,120,7,20],[151,0,17.1,149,8,20]]
    
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
    sup=2
    wi=0;l=2
    Ext=(wi*2)+P
    W+=wi
    L+=l
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
    wi=1;l=0
    L+=l
    W+=wi
    Ext=(wi*2)+P
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
    sup=2;l=1
    L+=l
    wi=1
    W+=wi
    Ext=(wi*2)+P
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
    sup=1
    wi=1;l=0
    L+=l
    W+=wi
    Ext=(wi*2)+P
    RCB.append(M)
    RCB.append(W)
    RCB.append(L)
    RCB.append(NoR)
    RCB.append(NRR)
    RCB.append(Ext)


    #RR
    NoR=0
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
    style = ttk.Style()
    style.theme_use('clam')
    tree = ttk.Treeview(win, column=("Pos", "Team", "M","W","L","N/R","NRR","Pts"), show='headings', height=8)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Pos")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Team")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="M")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="W")
    tree.column("# 5", anchor=CENTER)
    tree.heading("# 5", text="L")
    tree.column("# 6", anchor=CENTER)
    tree.heading("# 6", text="N/R")
    tree.column("# 7", anchor=CENTER)
    tree.heading("# 7", text="NRR")
    tree.column("# 8", anchor=CENTER)
    tree.heading("# 8", text="Pts")

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

        
        
        

