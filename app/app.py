import os
import json

from flask import Flask, render_template, request, redirect, url_for
from functools import lru_cache
from pymemcache.client import base


def json_serializer(key, value):
    if type(value) == str:
        return value, 1
    return json.dumps(value), 2


def json_deserializer(key, value, flags):
    if flags == 1:
        return value.decode("utf-8")
    if flags == 2:
        return json.loads(value.decode("utf-8"))
    raise Exception("Unknown serialization format")


client = base.Client(('35.187.180.236', 11211),
                     serializer=json_serializer,
                     deserializer=json_deserializer)


def is_positive_integer(string):
    try:
        int(string)
        if int(string) > 0:
            return True
        else:
            return False
    except ValueError:
        return False


@lru_cache()
def fibo_steroids(n):
    if n in [0, 1]:
        return n
    else:
        return fibo_steroids(n - 1) + fibo_steroids(n - 2)


def cache_data(num: int):
    if num in {1, 2}:
        return 1
    elif num > 2:
        cached_num = client.get(str(num))
        if cached_num is None:
            for x in range(3, num + 1):
                number = fibo_steroids(x)
                client.set(str(x), number)

            return client.get(str(num))
        else:
            return cached_num

    else:
        return "Вводите только положительные числа начиная с 1!!!"


app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        number = request.form.get('number')
        if is_positive_integer(number):
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
