from flask import Flask
from flask import request
from flask import render_template
# import users
import mysql.connector

# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine
# from sqlalchemy import text

app = Flask(__name__)

# cnx = mysql.connector.connect(user='test', password='password',
#                               host='127.0.0.1',
#                               database='ctf')
# cursor = cnx.cursor()

# query = ("SELECT password FROM ctf.users")
# where user_id = '1'
# sql = "SELECT password FROM ctf.users where user_id = " + 

# cursor.execute(query)
# for(password), in cursor:
#     print("{}".format(password))

# cnx.close()
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://test:password@localhost[:3306]/ctf'
# db = SQLAlchemy(app)
# mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>

# class User(db.Model):
#     username = db.Column(db.String(80), unique=True)
#     pw_hash = db.Column(db.String(80))

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     password = db.Column(db.String(10), primary_key=True)
    # def __init__(self, username, email):
    #     self.username = username
    #     self.email = email

    # def __repr__(self):
    #     return '<User %r>' % self.username


# sql = text('select pass from users where userid = :1')
# result = db.engine.execute('select pass from users where userid = :1')
# names = []
# for row in result:
#     names.append(row[0])

# print names

# cnx = mysql.connector.connect(user='test', password='password',
#                           host='127.0.0.1',
#                           database='ctf')
# cursor = cnx.cursor()
# names = "1"
# sql = "SELECT password FROM ctf.users where user_id = " + names
# print(sql)
# cursor.execute(sql)
# for(password), in cursor:
#     print("{}".format(password))
# cnx.close()

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/results', methods = ['POST'])
def results():
    # return render_template("results.html")
    # txtSQL = "SELECT * FROM Users WHERE UserId = "
    # txtSQL = "SELECT Key FROM Users WHERE UserId = " + names
    # table = {'1': 'a', '2': 'b', 'c': 'z', 'what_is_the_key': 'wow'}
    # table = {'1': '*oh_no_this_is_the_key*', '2': 'a', '3': 'b'}
    names = request.form['names']
    result = ""


    cnx = mysql.connector.connect(user='test', password='password',
                              host='127.0.0.1',
                              database='ctf')
    cursor = cnx.cursor()
    sql = "SELECT password FROM ctf.users where user_id = " + names
    # print(sql)
    cursor.execute(sql)
    for(password), in cursor:
        result += password
        # print("{}".format(password))
    cnx.close()


    #make other statements, like "or true/TRUE", turn it to lowercase
    #u must have an user id, so "7 or 1=1", not just "or 1=1"
    #implement some regex stuff

    try:
        names = int(names)
    except: 
        pass

    # sql_statements = "or 1=1" in names
    if names == 1:
        return render_template("error.html", names=names)
    # for word in table:
    # 	if names == word or sql_statements:
    # 		result += table[word]
    if result != "":
        return render_template("results.html", names=names, result=result)
    else:
    	return render_template("notexist.html", names=names)

if __name__ == "__main__":
    app.run()
    # app.debug = True