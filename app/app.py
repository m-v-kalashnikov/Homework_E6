import os
import sys

from flask import Flask, render_template, request
# Более правильный импорт. (Из документации pymemcache)
from pymemcache.client.base import Client

client = Client(('localhost', 11211))
# Максимальный лимит рекурсии, но лучше бы в данном случае вообще без неё.
sys.setrecursionlimit(2000)

# Ниже я сделал код короче.


def fibo_steroids(n):
    if n in [0, 1]:
        return n
    else:
        return fibo_steroids(n - 1) + fibo_steroids(n - 2)


app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))


@app.route('/')
def index():
    number = request.args.get('number')  # Меняем form на args, т.к у нас GET запрос.
    if number:
        if int(number) > 0:
            if client.get(number):
                return render_template('index.html', num=client.get(number).decode())
            else:
                result = fibo_steroids(int(number))
                client.set(number, str(result))
                return render_template('index.html', num=result)
        else:
            return render_template('index.html', num='Вводите только положительные числа!')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=bool(os.environ.get("DEBUG", True)),
            host='0.0.0.0', port=port)
