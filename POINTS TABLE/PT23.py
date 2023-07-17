#WAP to accept the inputs and print the NRR(Net Run Rate) of a team(If a team gets all out, the total overs is considered to be 20 overs)
#Tuple having the data form[Runs,wickets,overs,runs,wickets,overs]. 1st half comprises the own
# team and 2nd half for the opponent team
#Format for points table: Position, Team , Matches, Wins, Losses ,Points, NRR
from tkinter import *
from tkinter import ttk
import math
from operator import itemgetter
from tabulate import tabulate
def PT2023():
    CSK=[];MI=[];DC=[];KKR=[];PBKS=[];RCB=[];RR=[];SRH=[];LSG=[];GT=[]
    CSK.append("Chennai Super Kings")
    MI.append("Mumbai Indians")
    SRH.append("Sunrises Hyderabad")
    KKR.append("Kolkata Knight Riders")
    PBKS.append("Punjab Kings")
    RR.append("Rajasthan Royals")
    RCB.append("Royal Challengers Bangalore")
    DC.append("Delhi Capitals")
    LSG.append("Lucknow Super Giants")
    GT.append("Gujarat Titans")

    M=0;W=0;L=0
    Che=[[178,7,20,182,5,19.2],[217,7,20,205,7,20],[159,3,18.1,157,8,20],[172,6,20,175,8,20],[226,6,20,218,8,20],[138,3,18.4,134,7,20],[235,4,20,186,8,20],[170,6,20,202,5,20],[200,4,20,201,6,20],['N','I','L','N','I','L'],[140,4,17.4,139,8,20],[167,8,20,140,8,20],[144,6,20,147,4,18.3],[223,3,20,146,9,20]]
    Mum=[[171,7,20,172,2,16.2],[157,8,20,159,3,18.1],[173,4,20,172,10,19.4],[186,5,17.4,185,6,20],[192,5,20,178,10,19.5],[201,6,20,214,8,20],[152,9,20,207,6,20],[214,4,19.3,212,7,20],[216,4,18.5,214,3,20],[139,8,20,140,4,17.4],[200,4,16.3,199,6,20],[218,5,20,191,8,20],[172,5,20,177,3,20],[201,2,18,200,5,20]]
    Del=[[143,9,20,193,6,20],[162,8,20,163,4,18.1],[142,9,20,199,4,20],[172,10,19.4,173,4,20],[151,9,20,174,6,20],[128,6,19.2,127,10,20],[144,9,20,137,6,20],[188,6,20,197,6,20],[130,8,20,125,6,20],[187,3,16.4,181,4,20],[140,8,20,167,8,20],[136,8,20,167,7,20],[213,2,20,198,8,20],[146,9,20,223,3,20]]
    Kol=[[146,7,16,153,5,16],[204,7,20,123,10,17.4],[207,7,20,204,4,20],[205,7,20,228,4,20],[185,6,20,186,5,17.4],[127,10,20,128,6,19.2],[186,8,20,235,4,20],[200,5,20,179,8,20],[179,7,20,180,3,17.5],[171,9,20,166,8,20],[182,5,20,179,7,20],[149,8,20,151,1,13.1],[147,4,18.3,144,6,20],[175,7,20,176,8,20]]
    Pun=[[153,5,16,146,7,16],[197,4,20,192,7,20],[143,9,20,145,2,17.1],[153,8,20,154,4,19.5],[161,8,19.3,159,8,20],[150,10,18.2,174,4,20],[214,8,20,201,6,20],[201,10,19.5,257,5,20],[201,6,20,200,4,20],[214,3,20,216,4,18.5],[179,7,20,182,5,20],[167,7,20,136,8,20],[198,8,20,213,2,20],[187,5,20,189,6,19.4]]
    Roy=[[172,2,16.2,171,7,20],[123,10,17.4,204,7,20],[212,2,20,213,9,20],[174,6,20,151,9,20],[218,8,20,226,6,20],[174,4,20,150,10,18.2],[189,9,20,182,6,20],[179,8,20,200,5,20],[126,9,20,108,10,19.5],[181,4,20,187,3,16.4],[199,6,20,200,4,16.3],[171,5,20,59,10,10.3],[187,2,19.2,186,5,20],[197,5,20,198,4,19.1]]
    Raj=[[203,5,20,131,8,20],[192,7,20,197,4,20],[199,4,20,142,9,20],[175,8,20,172,6,20],[179,7,19.2,177,7,20],[144,6,20,154,7,20],[182,6,20,189,9,20],[202,5,20,170,6,20],[212,7,20,214,4,19.3],[118,10,17.5,119,1,13.5],[214,2,20,217,6,20],[151,1,13.1,149,8,20],[59,10,10.3,171,5,20],[189,6,19.4,187,5,20]]
    Sun=[[131,8,20,203,5,20],[121,8,20,127,5,16],[145,2,17.1,143,9,20],[228,4,20,205,7,20],[178,10,19.5,192,5,20],[134,7,20,138,3,18.4],[137,6,20,144,9,20],[197,6,20,188,6,20],[166,8,20,171,9,20],[217,6,20,214,2,20],[182,6,20,185,3,19.2],[154,9,20,188,9,20],[186,5,20,187,2,19.2],[200,5,20,201,2,18]]
    Luc=[[193,6,20,143,9,20],[205,7,20,217,7,20],[127,5,16,121,8,20],[213,9,20,212,2,20],[159,8,20,161,8,19.3],[154,7,20,144,6,20],[128,7,20,135,6,20],[257,5,20,201,10,19.5],[108,10,19.5,126,9,20],['N','I','L','N','I','L'],[171,7,20,227,2,20],[185,3,19.2,182,6,20],[177,3,20,172,5,20],[176,8,20,175,7,20]]
    Guj=[[182,5,19.2,178,7,20],[163,4,18.1,162,8,20],[204,4,20,207,7,20],[154,4,19.5,153,8,20],[177,7,20,179,7,19.2],[135,6,20,128,7,20],[207,6,20,152,9,20],[180,3,17.5,179,7,20],[125,6,20,130,8,20],[119,1,13.5,118,10,17.5],[227,2,20,171,7,20],[191,8,20,218,5,20],[188,9,20,154,9,20],[198,4,19.1,197,5,20]]

    #CSK
    NoR=0
    aa=[];bb=[];cc=[];dd=[];ee=[];ff=[]
    for i in Che:
        if i[0]=='N':
            NoR+=1
        else:
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
        if i[0]=='N':
            NoR+=1
        else:
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
        if i[0]=='N':
            NoR+=1
        else:
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
        if i[0]=='N':
            NoR+=1
        else:    
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
        if i[0]=='N':
            NoR+=1
        else:
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
        if i[0]=='N':
            NoR+=1
        else:
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
    NoR=0
    gg=[];hh=[];ii=[];jj=[];kk=[];ll=[];M=0;W=0;L=0;NRR=0
    for i in Raj:
        if i[0]=='N':
            NoR+=1
        else:
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
        if i[0]=='N':
            NoR+=1
        else:
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

    #LSG
    NoR=0
    gg=[];hh=[];ii=[];jj=[];kk=[];ll=[];M=0;W=0;L=0;NRR=0
    for i in Luc:
        if i[0]=='N':
            NoR+=1
        else:
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
    LSG.append(M)
    LSG.append(W)
    LSG.append(L)
    LSG.append(NoR)
    LSG.append(NRR)
    LSG.append(Ext)

    #GT
    NoR=0
    gg=[];hh=[];ii=[];jj=[];kk=[];ll=[];M=0;W=0;L=0;NRR=0
    for i in Guj:
        if i[0]=='N':
            NoR+=1
        else:
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
    GT.append(M)
    GT.append(W)
    GT.append(L)
    GT.append(NoR)
    GT.append(NRR)
    GT.append(Ext)



    OVR=[]
    OVR.append(CSK)
    OVR.append(DC)
    OVR.append(KKR)
    OVR.append(MI)
    OVR.append(PBKS)
    OVR.append(RCB)
    OVR.append(RR)
    OVR.append(SRH)
    OVR.append(LSG)
    OVR.append(GT)

    abc=sorted(OVR, key=itemgetter(6,5),reverse=True)
    Pos=[1,2,3,4,5,6,7,8,9,10]
    for i in range(1,11):
        abc[i-1].insert(0,i)


    win = Tk()
    win.geometry("700x350")

    colu=["Position", "Team", "Matches","Wins","Losses","No Result","Net Run Rate","Points"]
    tree = ttk.Treeview(win, column=("Position", "Team", "Matches","Wins","Losses","No Result","Net Run Rate","Points"), show='headings', height=10)
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
    tree.insert('', 'end', text="1", values=(abc[8][0], abc[8][1],abc[8][2],abc[8][3],abc[8][4],abc[8][5],abc[8][6],abc[8][7] ))
    tree.insert('', 'end', text="1", values=(abc[9][0], abc[9][1],abc[9][2],abc[9][3],abc[9][4],abc[9][5],abc[9][6],abc[9][7] ))
 
    tree.pack()

    win.mainloop()

    
    

