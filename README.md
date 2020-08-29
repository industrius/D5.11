Для проверки задания локально:

1. Стянуть репозиторий к себе в каталог виртуального окружения и активировать его.


2. Установить зависимости из requirements.txt:

pip install -r requirements.txt


3. Перейти в каталог проекта:

cd library_project


3. Выполнить миграции для создания БД:

python manage.py migrate


4. Импортировать в БД данные:

python manage.py loaddata data.xml


3. Запустить сервер:

python manage.py runserver


4. Открыть URL и наслаждаться;)


P.S. Для входа в "админку" не забудьте сгенерировать себе логин/пароль:

python manage.py createsuperuser