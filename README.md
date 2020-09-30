Запуск
1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py create_permissions `создает группы manager и worker(если их нет) и выдает им права`
6. python manage.py runserver

Эндпоинты:
- / `дом, если выполнен вход, то редиректит на /tickets`
- /login `вход`
- /logout `выход`
- /signin `регистрация`
- /tickets `страница заявок`
- /tickets/add `создание заявки`
- /tickets/id=\<id> `страница заявки`
- /tickets/id=\<id>/edit `редактирование заявки`

Роли:
- manager `может создавать и редактировать новые заявки`
- worker `может закрывать заявки`