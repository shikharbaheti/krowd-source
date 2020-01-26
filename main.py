from flask import Flask, render_template, jsonify, request
# from flask_mysqldb import MySQL
# import string_match as sm
import json
import pandas as pd

app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '0109'
# app.config['MYSQL_DB'] = 'krowd'

# mysql = MySQL(app)

# incidents=pd.read_csv("incidents.csv")
# print(incidents)


@app.route("/", methods=['GET', 'POST'])
def index():
    incidents = pd.read_csv("incidents.csv")
    incidents = incidents.sort_values(by=["UPVOTES"], ascending=False)
    if request.method == "GET":
        # cur = mysql.connection.cursor()
        # cur = con.cursor()
        # cur.execute("SELECT * FROM incidents")
        # data = cur.fetchall()
        data = []
        for index, rows in incidents.iterrows():
            # Create list for the current row
            my_list = [index, rows.NAME, rows.UPVOTES]

            # append the list to the final list
            data.append(my_list)
        print(data)
        incidents.to_csv("incidents.csv", index=False)
        return render_template('index.html', incidents=data)

    # cur = mysql.connection.cursor()
    incidents = pd.read_csv("incidents.csv")
    print(type(request.form['is_up']))

    if request.form["is_up"] == "true":
        print("upvoted")
        id = int(request.form["id"])
        # print(type(id))
        # cur.execute("update incidents set upvotes = upvotes +1 where id = %d" %id)
        incidents.iloc[id, 1] = incidents.iloc[id, 1]+1

    else:
        print("downvoted")
        id = int(request.form["id"])
        # cur.execute("update incidents set upvotes = upvotes - 1 where id = %d" %id)
        incidents.iloc[id, 1] = incidents.iloc[id, 1]-1
    print(incidents)
    incidents.to_csv("incidents.csv", index=False)
    return render_template('index.html')


@app.route('/report', methods=['POST'])
def report():
    print("request added")
    print(request.form)
    incidents = pd.read_csv("incidents.csv")
    location = str(request.form["location"])
    incident = str(request.form["incident"])
    lat = 30.615530300000003
    lng = -96.33844570000001
    incidents = incidents.append(
        {'NAME': incident, 'UPVOTES': 1, 'LATITUDE': lat, 'LONGITUDE': lng}, ignore_index=True)
    # incidents = incidents.append(pd.Series([incident,1,lat,lng], index=incidents.columns ), ignore_index=True)
    # incidents=incidents.concat(pd.DataFrame([incident,1,lat,lng], index=incidents.columns ))
    print("incidents")
    incidents.to_csv("incidents.csv", index=False)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
