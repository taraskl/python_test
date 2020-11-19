Python 3.8

Запуск проекту:
1. Встановити пакети з файла requirements.txt командою: 'pip install -r requirements.txt' .
2. Зайти в каталог проекту і запустити командою: 'python manage.py runserver' .
3. Зайти в панель адміністування за посиланням: http://127.0.0.1:8000/admin/ (логін: admin, пароль: admin).
4. Імпорт користувачів з файла знаходиться в закладці Customers -> Import CSV.
5. Апі користувачів доступне за посиланням: http://127.0.0.1:8000/api/customers/ , 
фільтрація користувачів по даті реєстрації доступна за посиланням: http://127.0.0.1:8000/api/customers/<дата_реєстаціє> . 