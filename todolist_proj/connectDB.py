import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.0.104",
    user="",
    password="",
    database=""
)

mycursor = mydb.cursor()

def get_todolist():
    sql = 'select * from todolist'
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result

def login(u,p):
    sql = 'select username,password from user where username=%s and password=%s'
    val = (u,p)
    mycursor.execute(sql,val)
    result = mycursor.fetchone()
    if len(result) == 1:
        return True
    # # Check that we found a user and verify the hashed password
    # if result and bcrypt.checkpw(p.encode(), result['password'].encode()):
    #     return True
    # return False
