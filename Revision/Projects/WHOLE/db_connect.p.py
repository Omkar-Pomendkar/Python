from flask import Flask , request, jsonify
import mysql.connector as conn

app = Flask(__name__)

mydb = conn.connect( host = "localhost",user="root",password="sS123456%")

cursor = mydb.cursor()
cursor.execute("Create Database if not exists tasksql")
cursor.execute("Create table if not exists tasksql.mysqltable(name varchar(30) , number int)")


@app.route ('/insert',methods = ['POST'])
def insert():
    if request.method == "POST":
        name = request.json['name']
        number = request.json['number']
        cursor.execute("Insert into tasksql.mysqltable values (%s , %s)" , (name,number))
        mydb.commit()
        return jsonify(str("Succesfully Inserted"))

@app.route ('/update',methods = ['POST'])
def update():
    if request.method == "POST":
        get_name = request.json['get_name']
        cursor.execute("Update tasksql.mysqltable set number = number+500 where name = %s",(get_name,))
        mydb.commit()
        return jsonify(str("Updated Successfully"))

@app.route('/delete',methods=["POST"])
def delete():
    if request.method == "POST":
        del_name = request.json['del_name']
        cursor.execute(" delete from tasksql.mysqltable where name = %s",del_name)
        mydb.commit()
        return jsonify(str("Deleted Successfully"))
@app.route("/fetchall",methods = ['POST','GET'])
def fetch_data():
    cursor.execute("select * from tasksql.mysqltable ")
    l = []
    for i in cursor.fetchall():
        l.append(i)
    return jsonify(str(l))







if __name__== "__main__":
    app.run()