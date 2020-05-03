# BASH:

Ключи:

`-a - Общее количество запросов`

`-b - Количество запросов по типу`

`-c - Топ 10 самых больших по размеру запросов`

`-d - Топ 10 запросов по количеству, которые завершились клиентской ошибкой`

`-e - Топ 10 запросов клиентских ошибок по размеру запроса`

`-h - Помощь`

При выборе любого ключа скрипт попросит указать путь до файла или директории.
Пример:

`/Users/igorkhotyanovich/projects/2020-1-Atom-QA-Python-I-Khotianovich/Home_task3/data/nginx_logs_1.log`

или

`/Users/igorkhotyanovich/projects/2020-1-Atom-QA-Python-I-Khotianovich/Home_task3/data`


Укажите его и нажмите return.


Результат будет записан в файл формата: `res-'ключ'.txt`

_____

Keys:


`-a - Total number of requests`

`-b - Number of queries by type`

`-c - Top 10 Biggest Queries`

`-d - Top 10 quantity requests that ended with a client error`

`-e - Top 10 requests that ended with a client error by size`

`-h - Help`



The script asked for the path to the file or directory.
Example:

`/Users/igorkhotyanovich/projects/2020-1-Atom-QA-Python-I-Khotianovich/Home_task3/data/nginx_logs_1.log`

or

`/Users/igorkhotyanovich/projects/2020-1-Atom-QA-Python-I-Khotianovich/Home_task3/data`


Specify it and click "return".


The result will be written to a format file: `res-'key'.txt`

# Python:

Запустите parse.py и просто следуйте диалоговому окну.

_____

Run parse.py and just follow the dialog box.


# MySQL:

Для записи парсинга логов в БД укажите путь к файлу/директории в файле tests/test_orm_mysql.py (строка 14).
Затем запустите:
 `pytest -s -l -v -m 'db_log' ` 
 Результат будет в БД `igor_test_db`
 _____
 
To record log parsing in the database, specify the path to the file / directory in the tests / test_orm_mysql.py file (line 14).
Then run:
 `pytest -s -l -v -m 'db_log' ` 
 Result will be in `igor_test_db`
