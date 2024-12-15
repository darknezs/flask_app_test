import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.0.107",
    user="",
    password="",
    database=""
)

mycursor = mydb.cursor()


def getAll():
    sql = "select * from birthday"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return data

def insert_2_db(band, name, bd):
    sql = "INSERT INTO birthday(band, name, birthday) values(%s,%s,%s)"
    val = (band, name, bd)
    mycursor.execute(sql,val)
    mydb.commit()
    print(f"INSERT COMPLETE : {mycursor.rowcount}")

def delete_data(id):
    sql = "DELETE FROM birthday WHERE id = %s"
    val = (id,)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

def update(id,name,band,bd):
    sql="UPDATE birthday SET name = %s, band=%s, birthday=%s WHERE id = %s"
    val=(name, band, bd, id)
    mycursor.execute(sql,val)
    mydb.commit()
    print('update effect ', mycursor.rowcount, ' rows')
