from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector as connector

db = connector.connect(host="localhost", user="root", passwd="root", database="register")

app = Flask(__name__, template_folder='templates')
app.secret_key = "fsggrsgsrgrg"


# @app.route('/')
# def hello_world():
#     return redirect(url_for("result"))

@app.route('/home')
def hello_world():
    return redirect(url_for('Base.html'))


# @app.route('/')
# def hello_world():
#     return render_template("index.html")
# @app.route('/')
# def hello_world():
#     return render_template("index.html")\
#
# @app.route('/')
# def hello_world():
#     return render_template("index.html")
@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        country = request.form["country"]
        password = request.form["password"]

        print(name, email, country, password)
        cursor = db.cursor()
        sql = "INSERT INTO `delegates`(`name`, `email`, `country`, `password`) VALUES (%s,%s,%s,%s)"
        val = (name, email, country, password)
        cursor.execute(sql, val)
        db.commit()
        flash("saved in database")
        redirect(url_for('show_register'))
    return render_template('form.html')


# show Pleople Registered
@app.route('/show_register')
def show_register():
    # if session.get('names') == None:
    #     return redirect(url_for('login'))
    cursor = db.cursor()
    sql = "SELECT * FROM delegates"
    cursor.execute(sql)
    delegates = cursor.fetchall()
    return render_template('form_output.html', delegates=delegates)


@app.errorhandler(404)
def error_page(e):
    # print("error")
    return render_template('error.html')


if __name__ == '__main__':
    app.run(port=8000, debug=True)
