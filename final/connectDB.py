import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

mydb = mysql.connector.connect(
    host = os.getenv("host"),
    username = os.getenv("user"),
    password = os.getenv("password"),
    database = os.getenv("database")
)

mycursor = mydb.cursor()

def insert2Db(rec, hell, ih, nmd, tree, pit):
    print("insert2Db")
    sql = "INSERT INTO final(resource ,helltide ,ih ,nmd ,tree ,pit) values(%s,%s,%s,%s,%s,%s)"
    val = (rec, hell, ih, nmd, tree, pit)
    mycursor.execute(sql,val)
    mydb.commit()
    print(f'insert :  {mycursor.rowcount} row')

def get_data():
    mydb.commit()
    sql = "select * from final"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return data

def update_data(hell, ih, nmd, tree, pit ,id):
    print('from update')
    sql = 'update final set helltide=%s ,ih=%s ,nmd=%s ,tree=%s ,pit=%s where id=%s'
    val = (hell, ih, nmd, tree, pit ,id)
    mycursor.execute(sql,val)
    mydb.commit()
    print(f'updated {mycursor.rowcount} row')
    return True

def add_user(usr,psd):
    sql = 'INSERT into user(username,password) values(%s,%s)'
    val = (usr,psd)
    mycursor.execute(sql,val)
    mydb.commit()
    if mycursor.rowcount == 1:
        return True

def getUser(id):
    sql = 'select user_id,username,password from user where user_id = %s'
    val = (id,)
    mycursor.execute(sql,val)
    data = mycursor.fetchone()
    return data

def getLogin(username):
    sql = 'select * from user where %s'
    val = (username,)
    mycursor.execute(sql,val)
    data = mycursor.fetchone()
    return data 
