from flask import Flask
from flask import jsonify
from flask import flash, request
from flask_mysqldb import MySQL

#app configuration
app = Flask(__name__)
app.secret_key = "test"
#db conffiguration
app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "test"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
#Mysql Connection
mysql = MySQL(app)

#Get Method
@app.route('/home')
def home():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM DUAL")
    rows = cursor.fetchall()
    resp=jsonify(rows)
    resp.status_code=200
    return resp

#Post Method
@app.route('/add',methods=['POST'])
def post():
    json = request.json()
	name=json['name']
    email=json['email']
    if name and email and equest.method=='POST':
        cursor = mysql.connection.cursor()
        query='INSERT INTO TABLE(user_name, user_email) VALUES(%s,%s)'
        cursor.execute(query, (name, email))
        mysql.connection.commit()
        resp = jsonify("User has been added successfully")
        resp.status_code=200
        print(resp)
    else:
        print("Not Found!")
        cursor.close()

#Delete Method
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM TABLE WHERE user_id=%s", (id,))
    mysql.connection.commit()
    cursor.close()
    resp=jsonify("User has been deleted successfully")
    resp.status_code=200
    return resp

#Put Method
@app.route('/update/<int:id>', methods=['PUT'])
def update_user(id):
    json=request.json()
    email=json['email']
    if id and email and request.method=='PUT':
        query="UPDATE TABLE SET user_email=%s WHERE user_id=%s"
        cursor = mysql.connection.cursor()
        cursor.execute(query, (email, id))
        mysql.connection.commit()
        resp = jsonify('User updated successfully!')
        resp.status_code=200
        cursor.close()
    else:
        print("Error")


if __name__ == "__main__":
    app.run()
