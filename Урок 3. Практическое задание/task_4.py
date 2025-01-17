"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
import hashlib
from uuid import uuid4
cache_dict = {}
salt = uuid4().hex

def cache_page(url):
    if url not in cache_dict.keys():
        cache_dict[url] = hashlib.sha256(salt.encode()+url.encode()).hexdigest()
    else:
        print('Страница уже закеширована')
    return


cache_page('http://ya.ru')
cache_page('http://ya.ru')