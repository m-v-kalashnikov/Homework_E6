import os

from flask import Flask, render_template, request, redirect, url_for

from app.fibonacci import cache_data, is_positiv_integer

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        number = request.form.get('number')
        if is_positiv_integer(number):
            return redirect(url_for('index_fibo', num=number))
        else:
            return redirect(url_for('index_fibo', num=-1))
    else:
        return render_template('index.html')


@app.route('/<num>')
def index_fibo(num):
    number = cache_data(int(num))
    return render_template('index.html', num=number)


if __name__ == '__main__':
    app.run(debug=bool(os.environ.get("DEBUG", True)), host='0.0.0.0', port=port)
