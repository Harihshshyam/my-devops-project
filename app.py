from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def counter():
    if os.path.exists('counter.txt'):
        count = int(open('counter.txt').read())
    else:
        count = 0
    if request.method == 'POST':
        count += 1
        open('counter.txt','w').write(str(count))
    return jsonify({"count": count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

