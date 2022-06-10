from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'test'
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)
 
@app.route('/form')
def form():
    # conn = mysql.connect()
    # cursor = mysql.connection.cursor()
    # cursor.execute("SELECT * FROM student")
    # data = cursor.fetchone()
    # for item in data:
    #     print(item)
    return render_template('form.htm')
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['name']
        # age = request.form['age']
        cursor = mysql.connection.cursor()
        # print( "INSERT INTO student VALUES ('{0}')".format(name))
        cursor.execute("INSERT INTO student VALUES ('{0}')".format(name))
        mysql.connection.commit()
        cursor.close()
        # return "INSERT INTO student VALUES ('{0}')".format(name)
        return "Done!!"
 
app.run(host='localhost', port=5000)