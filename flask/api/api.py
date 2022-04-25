import flask
from flask import jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS


app = flask.Flask(__name__)
app.config["DEBUG"] = True



app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'JuanSoto^%OPS+'
app.config['MYSQL_DB'] = 'gpu'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Price LIMIT 100")
    row_headers=[x[0] for x in cursor.description]
    rv = cursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return jsonify(json_data)

@app.route('/poo', methods=['GET'])
def poo():
    return "<h1>peeeee Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/test', methods = ['GET'])
def test():
    return jsonify('test')




app.run()