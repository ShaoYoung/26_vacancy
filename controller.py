# Обработка событий от пользователя, изменение модели

import model as mod
import view as v


# начало работы controller, инициализация БД
def start_work():
    file_name = 'Data_base.db'
    mod.init_db(file_name)


# просмотр БД
def preview_base():
    info = mod.get_info('SELECT * FROM work')
    v.print_db(info)


# добавление информации в БД
def add_vacancy():
    # получаем новую запись БД
    vacancy = list(v.get_data().values())
    mod.add_record('INSERT INTO work VALUES(?, ?, ?, ?, ?);', vacancy)


# поиск информации в БД
def find_vacancy(find_vac):
    info = mod.find_record(f'SELECT * FROM work WHERE name LIKE "{find_vac}"')
    if len(info):
        print('Нашёл:')
        v.print_db(info)
        return info
    else:
        print('Запрашиваемой информации нет в БД!')
        return []


# поиск информации в БД по пяти буквам
def find_vacancy_5_let(find_vac_5_let):
    info = mod.get_info('SELECT * FROM work')
    finded_info = []
    # перебираем все вакансии из БД
    for vacancy in info:
        # если в названии вакансии есть подстрока из искомых 5 букв, то добавляем вакансию в список найденных
        if vacancy[0].find(find_vac_5_let) != -1:
            finded_info.append(vacancy)
    if len(finded_info):
        print('Нашёл:')
        v.print_db(finded_info)
    else:
        print('Запрашиваемой информации нет в БД!')


# удаление информации из БД
def del_vacancy(del_vac):
    # ищем запись БД
    info = find_vacancy(del_vac)
    # если есть записи БД
    if len(info):
        # контрольный вопрос для подтверждения удаления записи
        accept_delete = input('Удаляем? 1 - Да, 0 - Нет: --> ')
        if int(accept_delete):
            mod.modify_record(f'DELETE FROM work WHERE name = "{del_vac}"')
