from flask import Flask
from flask import request
import random, time
import mysql.connector
import os

app = Flask(__name__)

first_name = 'John'
last_name = 'Smith'

cnx = mysql.connector.connect(user='aman', password='aman123',
                              host='localhost',
                              database='test2')
cursor = cnx.cursor()

def get_file_content():
    path = "/home/tshoot/get_file.txt"
    if os.path.exists(path):
        os.remove(path)
    
    with open(path, 'a+') as file:
        for i in range(100000):
            file.write(str(i))

    with open(path, 'r') as file:
        return file.readline()

def update_table(fname, lname, roll_no):
    query = f"update Student set fname='{fname}',lname='{lname}' where roll_no={roll_no};"
    cursor.execute(query)
    cnx.commit()

def delete_from_table(fname, lname, roll_no):
    query = f"delete from Student where roll_no={roll_no};"
    cursor.execute(query)
    cnx.commit()

def write_to_table(fname, lname, roll_no):
    query = f"insert into Student values('{roll_no}','{fname}','{lname}');"
    cursor.execute(query)
    cnx.commit()

@app.route('/', methods = ['GET'])
def user():
    return get_file_content()

@app.route('/chaos', methods = ['GET'])
def chaos():
    while True:
        for roll in range(1000):
            write_to_table(first_name, last_name, roll)
        for roll in range(1000):
            delete_from_table(first_name, last_name, roll)


app.run()

        