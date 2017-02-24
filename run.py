from flask import Flask
from flask import request
from flask import render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/results', methods = ['POST'])
def results():
    names = request.form['names']
    names = names.lower()
    passwords = request.form['passwords']
    result = ""

    #user info
    user_id = None
    user_password = None
    user_name = None

    try:
        connection = mysql.connector.connect(user='test', password='password',
                                  host='127.0.0.1',
                                  database='ctf')
        cursor = connection.cursor()
        # 'SELECT * FROM Users WHERE Name ="' + uName + '" AND Pass ="' + uPass + '"'
        # 'SELECT * FROM ctf.users WHERE name ="' names + '" AND password ="' + passwords + '"'
        # cow = 'SELECT * FROM ctf.users WHERE name =\"' + names + '\" AND password =\"' + passwords + '\"'
        # print(cow)
        user_sql = "SELECT * FROM ctf.users where name = \'" + names + "\'"
        pass_sql = " AND password = \'" + passwords + "\'"
        sql = user_sql + pass_sql
        # print(sql)
        # execute multiple sql statements to allow for sql injection
        results = cursor.execute(sql, multi=True)
        # loop through all statements
        # for each value, set the password
        # for cur in results:
        #     if cur.with_rows:
        #         for values in cur.fetchall():
        #             print(values)
        #             for password in values:
        #                 print(password)
        #                 result = password

        # print(results[0][0])
        for cur in results:
            if cur.with_rows:
                # print(cur.fetchall())
                nest = cur.fetchall()
                print(nest)
                # print("user_id: " nest[0][0])
        if(len(nest) != 0):
            user_id = nest[0][0]
            user_password = nest[0][1]
            user_name = nest[0][2]
            result = "a"
        # print(results)
        connection.close()

    # should return an error if query doesn't work
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        return render_template("input_error.html")

    #Change it to two input fields
        #-user, so it is a specific person
        #-password, where the person can do sql injection to get the password
    #if the number input is the 10, goes to error page
    #if the result value isn't change, goes to not exist page
    #FIGURE OUT joe' and 1=1; -- a
    if ''.join(names.split()) == "joe" and user_password != passwords:
        names = ''.join(names.split())
        return render_template("error.html", names=names)
    if result != "":
        return render_template("results.html", names=names, result=user_password)
    else:
    	return render_template("notexist.html", names=names)

if __name__ == "__main__":
    app.run()
    # app.debug = True