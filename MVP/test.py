import mysql.connector as pro
con=pro.connect(host='localhost',user='root',passwd='Titan@1212',database='ipl')
cur=con.cursor()
cur.execute('use ipl')
cur.execute("Select * from mvp2019 where Player like '%Virat%'")
rows=cur.fetchall()
for i in rows:
    for j in i:
        print(j)
