from functools import lru_cache

from app.cache import client


def is_positiv_integer(string):
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
        return fibo_steroids(n-1) + fibo_steroids(n-2)


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
