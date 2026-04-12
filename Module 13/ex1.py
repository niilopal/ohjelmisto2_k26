from flask import Flask, request
app = Flask(__name__)
@app.route('/alkuluku/<num>')
def alkuluku(num):
    x = 0
    num = int(num)
    result = {
        'Number': num
    }
    for i in range(num):
        if num % (i + 1) == 0:
            x += 1
    if x == 2:
        result['isPrime'] = True
    else:
        result['isPrime'] = False
    return result

app.run(use_reloader=True, host='127.0.0.1', port=3000)