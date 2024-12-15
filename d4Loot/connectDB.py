import mysql.connector

mydb = mysql.connector.connect(
    host = "192.168.0.107" ,
    user = "",
    password = "",
    database = "",
)

mycursor = mydb.cursor()

def insert2db(helltide,ih,lboss,wboss,lgn,nmd,tree,dark,under,pit):
    #print(helltide,ih,lboss,wboss,lgn,nmd,tree,dark,under,pit)
    sql = 'INSERT INTO loot (helltide, ih, ladder_boss, world_boss, legion, nmd, tree, dark_cit, under_city, pit) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    val = (helltide,ih,lboss,wboss,lgn,nmd,tree,dark,under,pit)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record insert")


def getAll():
    sql = 'select * from loot'
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return (data)
