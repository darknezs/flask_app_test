import mysql.connector
from flask import jsonify
mydb = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)

mycursor = mydb.cursor()

def insert(name, dc_eng, summarize, dc_th):
    if type(dc_th) == float:
        dc_th = "empty"
    sql = "INSERT INTO data(method_name, desc_eng, summarize, desc_th) values(%s,%s,%s,%s)"
    val = (name, dc_eng, summarize, dc_th)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


def select():
    print("**** from select ****")
    sql = "SELECT * FROM data"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    # print("\n******  from method select  ******\n")
    # for x in result:
    #     print(x)
    return result

def updateDB(data):
    print("**** from updateDB ****")
    for row in data:

        # sql = "UPDATE data SET desc_eng = %s, summarize = %s, desc_th = %s WHERE method_name = %s"
        # val = (row['desc_eng'], row['summarize'], row['desc_th'], row['method_name'])
        sql = "UPDATE data SET method_name = %s, desc_eng = %s, summarize = %s, desc_th = %s WHERE id = %s"
        val = (row['method_name'], row['desc_eng'], row['summarize'], row['desc_th'],row['id'])
        mycursor.execute(sql, val)
    mydb.commit()
