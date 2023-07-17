#WAP to accept the inputs and print the NRR(Net Run Rate) of a team(If a team gets all out, the total overs is considered to be 20 overs)
#Tuple having the data form[Runs,wickets,overs,runs,wickets,overs]. 1st half comprises the own team and 2nd half for the opponent team
#Format for points table: Position, Team , Matches, Wins, Losses ,Points, NRR
from tkinter import *
from tkinter import ttk
import math
from operator import itemgetter
def PT2021():
    CSK=[];MI=[];DC=[];KKR=[];PBKS=[];RCB=[];RR=[];SRH=[]
    CSK.append("Chennai Super Kings")
    MI.append("Mumbai Indians")
    SRH.append("Sunrises Hyderabad")
    KKR.append("Kolkata Knight Riders")
    PBKS.append("Punjab Kings")
    RR.append("Rajasthan Royals")
    RCB.append("Royal Challengers Bangalore")
    DC.append("Delhi Capitals")


    M=0;W=0;L=0
    Che=[[188,7,20,190,3,18.4],[107,4,15.4,106,8,20],[188,9,20,143,9,20],[220,3,20,202,10,19.1],[191,4,20,122,9,20],[173,3,18.3,171,3,20],[218,4,20,219,6,20],[156,6,20,136,8,20],[157,4,18.1,156,6,20],[172,8,20,171,6,20],[139,4,19.4,134,7,20],[189,4,20,190,3,17.3],[136,5,20,139,7,19.4],[134,6,20,139,4,13]]
    Mum=[[159,9,20,160,8,20],[152,10,20,142,7,20],[150,5,20,137,10,19.4],[137,9,20,138,4,19.1],[131,6,20,132,1,17.4],[172,3,18.3,171,4,20],[219,6,20,218,4,20],[136,8,20,156,6,20],[155,6,20,159,3,15.1],[111,10,18.1,165,6,20],[137,4,19,135,6,20],[129,8,20,132,6,19.1],[94,2,8.2,90,9,20],[235,9,20,193,8,20]]
    Del=[[190,3,18.4,188,7,20],[147,8,20,150,7,19.4],[198,4,18.2,195,4,20],[138,4,19.1,137,9,20],[159,4,20,159,7,20],[170,4,20,171,5,20],[156,3,16.3,154,6,20],[167,3,17.4,166,6,20],[139,2,17.5,134,9,20],[154,6,20,121,6,20],[127,9,20,130,7,18.2],[132,6,19.1,129,8,20],[139,7,19.4,136,5,20],[164,5,20,166,3,20]]
    Kol=[[187,6,20,177,5,20],[142,7,20,152,10,20],[166,8,20,204,4,20],[202,10,19.1,220,3,20],[133,9,20,134,4,18.5],[126,5,16.4,123,9,20],[154,6,20,156,3,16.3],[94,1,10,92,10,19],[159,3,15.1,155,6,20],[171,6,20,172,8,20],[130,7,18.2,127,9,20],[165,7,20,168,5,19.3],[119,4,19.4,115,8,20],[171,4,20,85,10,16.1]]
    Pun=[[221,6,20,217,7,20],[106,8,20,107,4,15.4],[195,4,20,198,4,18.2],[120,10,19.4,121,1,18.4],[132,1,17.4,131,6,20],[123,9,20,126,5,16.4],[179,5,20,145,8,20],[166,6,20,167,3,17.4],[183,4,20,185,10,20],[125,7,20,120,7,20],[135,6,20,137,4,19],[168,5,19.3,165,7,20],[158,6,20,164,7,20],[139,4,13,134,6,20]]
    Roy=[[160,8,20,159,9,20],[149,8,20,143,9,20],[204,4,20,166,8,20],[181,0,16.3,177,9,20],[122,9,20,191,4,20],[171,5,20,170,4,20],[145,8,20,179,5,20],[92,10,19,94,1,10],[156,6,20,157,4,18.1],[165,6,20,111,10,18.1],[153,3,17.1,149,9,20],[164,7,20,158,6,20],[137,6,20,141,7,20],[166,3,20,164,5,20]]
    Raj=[[217,7,20,221,6,20],[150,7,19.4,147,8,20],[143,9,20,188,9,20],[177,9,20,181,0,16.3],[134,4,18.5,133,9,20],[171,4,20,172,3,18.3],[220,3,20,165,8,20],[185,10,20,183,4,20],[121,6,20,154,6,20],[164,5,20,167,3,18.3],[149,9,20,153,3,17.1],[190,3,17.3,189,4,20],[90,9,20,94,2,8.2],[85,10,16.1,171,4,20]]
    Sun=[[177,5,20,187,6,20],[143,9,20,149,8,20],[137,10,19.4,150,5,20],[121,1,18.4,120,10,19.4],[159,7,20,159,4,20],[171,3,20,173,3,18.3],[165,8,20,220,3,20],[134,9,20,139,2,17.5],[120,7,20,125,7,20],[167,3,18.3,164,5,20],[134,7,20,139,4,19.4],[115,8,20,119,4,19.4],[141,7,20,137,6,20],[193,8,20,235,9,20]]

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
    sup=0
    wi=0;l=0
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
    sup=0
    wi=0;l=0
    L+=l
    W+=wi
    Ext=(wi*2)+P
    KKR.append(M)
    KKR.append(W)
    KKR.append(L)
    KKR.append(NoR)
    KKR.append(NRR)
    KKR.append(Ext)

    #PBKS
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
    PBKS.append(M)
    PBKS.append(W)
    PBKS.append(L)
    PBKS.append(NoR)
    PBKS.append(NRR)
    PBKS.append(Ext)

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
    OVR.append(PBKS)
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

        
        

