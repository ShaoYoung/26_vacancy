import sqlite3

# глобальные переменные
db = None
cursor = None


# инициализация начальных значений переменных db, cursor, чтобы не передавать в каждую функцию, создание таблицы БД
def init_db(file_name):
    global db, cursor
    db = sqlite3.connect(file_name)
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS work(
        name TEXT,
        skills TEXT,
        description TEXT,
        salary INT,
        type TEXT)'''
                   )


# получение информации из БД по запросу sql_qwery. на выходе список кортежей
def get_info(sql_qwery):
    cursor.execute(sql_qwery)
    info = cursor.fetchall()
    return info


# добавление записи в БД. на входе sql-запрос и данные
def add_record(sql_qwery, vacancy):
    cursor.execute(sql_qwery, vacancy)
    db.commit()


# поиск записи по запросу
def find_record(sql_qwery):
    # pass заглушка
    cursor.execute(sql_qwery)
    info = cursor.fetchall()
    return info


# изменение записи из БД. на входе sql-запрос
def modify_record(sql_qwery):
    cursor.execute(sql_qwery)
    db.commit()
