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
    result = ""

    try:
        connection = mysql.connector.connect(user='test', password='password',
                                  host='127.0.0.1',
                                  database='ctf')
        cursor = connection.cursor()
        sql = "SELECT password FROM ctf.users where name = \'" + names + "\'"
        print(sql)
        # execute multiple sql statements to allow for sql injection
        results = cursor.execute(sql, multi=True)
        # loop through all statements
        # for each value, set the password
        for cur in results:
            if cur.with_rows:
                for values in cur.fetchall():
                    for password in values:
                        result += password

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
    if ''.join(names.split()) == "joe":
        names = ''.join(names.split())
        return render_template("error.html", names=names)
    if result != "":
        return render_template("results.html", names=names, result=result)
    else:
    	return render_template("notexist.html", names=names)

if __name__ == "__main__":
    app.run()
    # app.debug = True