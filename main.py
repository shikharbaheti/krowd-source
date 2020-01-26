from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL
# import string_match as sm
import json

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '0109'
app.config['MYSQL_DB'] = 'krowd'

mysql = MySQL(app)

@app.route("/", methods=['GET', 'POST'])
def index():
	print("hi")
	if request.method == "GET":
		cur = mysql.connection.cursor()
        # cur = con.cursor()
		cur.execute("SELECT * FROM incidents")
		data = cur.fetchall()
		print(data)
		return render_template('index.html', incidents=data)
    
	return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
