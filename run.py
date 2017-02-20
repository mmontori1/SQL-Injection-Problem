from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/results', methods = ['POST'])
def results():
    table = {'1': '*oh_no_this_is_the_key*', '2': 'a', '3': 'b'}
    names = request.form['names']
    result = ""

    for word in table:
      if names == word:
          result += table[word]

    if names == '1':
        return render_template("error.html", names=names)
    if result != "":
        return render_template("results.html", names=names, result=result)
    else:
    	return render_template("notexist.html", names=names)

if __name__ == "__main__":
    app.run()
    # app.debug = True