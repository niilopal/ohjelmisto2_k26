from flask import Flask
import mysql.connector
app = Flask(__name__)
@app.route('/kenttä/<icao>')
def kenttä(icao):
    c =mysql.connector.connect(
        host = "127.0.0.1",
        port = 3306,
        database = 'flight_game',
        user = 'username',
        password = 'password',
        autocommit = False
    )
    cur = c.cursor()
    cur.execute(f'select ident, name, municipality from airport where ident = "{icao}"')
    results = cur.fetchall()
    result = {
        'ICAO': results[0][0],
        'Name': results[0][1],
        'Municipality': results[0][2]
    }
    return result
app.run(use_reloader=True, host='127.0.0.1', port=3000)