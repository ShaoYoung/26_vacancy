# Работа с пользователем в терминале (ввод и отображение информации)
import controller as cont


# выбор действия пользователя БД
def input_action():
    while True:
        user_choice = input('1 - просмотреть все вакансии\n2 - добавить новую вакансию\n3 - найти вакансию по названию'
                            '\n4 - найти вакансию по пяти буквам\n5 - удалить вакансию\nq - выход \n-->> ')
        if user_choice == '1':
            cont.preview_base()
        elif user_choice == '2':
            cont.add_vacancy()
        elif user_choice == '3':
            find_vac = input('Введите название вакансии \n-->> ').lower()
            cont.find_vacancy(find_vac)
        elif user_choice == '4':
            find_vac_5_let = input('Введите пять букв вакансии \n-->> ').lower()
            cont.find_vacancy_5_let(find_vac_5_let)
        elif user_choice == '5':
            del_vac = input('Введите название вакансии \n-->> ').lower()
            cont.del_vacancy(del_vac)
        elif user_choice == 'q':
            print('Завершение работы')
            break
        else:
            print('Не корректный ввод!')


# печать БД. на входе список кортежей
def print_db(db):
    count = 0
    for vacancy in db:
        count += 1
        print(f'\033[31mВакансия № {count}: \033[0m')
        print(f'Наименование вакансии: {vacancy[0]}')
        print(f'Ключевые навыки: {vacancy[1]}')
        print(f'Описание: {vacancy[2]}')
        print(f'Зарплата: {vacancy[3]}')
        print(f'Вид работы: {vacancy[4]}')


# получение информации от пользователя
def get_data():
    print('Введите данные новой вакансии: ')
    # проверка корректности ввода и преобразование в int (salary и bonus)
    correct_salary = lambda x: int(x) if x.isdigit() and int(x) >= 0 else None
    correct_type = lambda x: x if x == "удалённый" or x == "смешанный" or x == "в офисе" else None
    vacancy = {
        'name': input('Наименование вакансии: ').lower(),
        'skills': input('Ключевые навыки: ').lower(),
        'description': input('Описание: ').lower(),
        # проверяем введённые данные и, если всё верно, преобразуем в INT, т.к. поле БД INT
        'salary': correct_salary(input('Зарплата: ')),
        # проверяем введённые данные и, если всё верно, записываем в БД, т.к. поле БД может иметь только три значения
        'type': correct_type(input('Вид работы (удалённый, смешанный, в офисе): ').lower()),
    }
    return vacancy
