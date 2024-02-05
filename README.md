# backend_community_homework
Проект предназначен для отработки практических навыков работы с формами django и их тестированием

## Запуск проекта

Склонируйте репозитарий, создайте и активируйте виртуальное окружение, установите зависимости

```
git clone git@github.com:den-sad/hw03_forms.git
cd hw03_forms

python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip intstall -r requirements.txt
```

Выполните миграции и запустите проект, при необходимости создайте суперпользователя 
для доступа в административную часть backend

```
python3 ./yatube/manage.py migrate
python3 ./yatube/manage.py createsuperuser
python3 ./yatube/manage.py runserver
```

## Запуск тестирования

```
pytest
```