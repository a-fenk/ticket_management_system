start
1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py create_permissions `create groups of manager and worker(if doesn't exists) and grants permissions to them`
6. python manage.py runserver

endpoints:
- / `home, if logged in, redirect to /tickets`
- /login `login`
- /logout `logout`
- /signin `registration / sign in`
- /tickets `tickets list`
- /tickets/add `add ticket`
- /tickets/id=\<id> `ticket page`
- /tickets/id=\<id>/edit `ticket editing`

Роли:
- manager `is able to create and edit ticket`
- worker `is able to close tickets`
