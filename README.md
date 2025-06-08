# ElectroNet

ElectroNet — это веб-приложение для управления сетью по продаже электроники, включая заводы, розничные сети и индивидуальных предпринимателей.

## Установка

### Предварительные требования

- Python 3.8+
- Django 5.2.2
- PostgreSQL (или другая база данных по вашему выбору)

### Шаги для установки

1. Клонируйте репозиторий:
   
bash
   git clone https://github.com/вашеимяпользователя/ElectroNet.git
   cd ElectroNet
   

2. Создайте и активируйте виртуальное окружение:
   
bash
   python -m venv env
   source env/bin/activate  # На Windows: env\Scripts\activate
   

3. Установите зависимости:
   
bash
   pip install -r requirements.txt
   

4. Настройте базу данных в файле `settings.py`.

5. Создайте миграции и примените их:
   
bash
   python manage.py makemigrations
   python manage.py migrate
   

6. Создайте суперпользователя для доступа к админ-панели:
   
bash
   python manage.py createsuperuser
   

7. Запустите сервер:
   
bash
   python manage.py runserver
   

## Использование

- Перейдите в админ-панель по адресу:
  
  http://127.0.0.1:8000/admin/
  

- Используйте API, доступный по адресу:
  
  http://127.0.0.1:8000/api/
  

### Документация API

- Swagger UI: 
  
  http://127.0.0.1:8000/swagger/
  

- ReDoc: 
  
  http://127.0.0.1:8000/redoc/
  

## Тестирование

Для запуска тестов используйте команду:
bash
python manage.py test

## Контакт для связи с командой разработки:
`tema124ru@mail.ru`


## Источники
Программа создана при поддержке онлайн-школы [skypro@skyeng.ru](https://sky.pro/#giftpopup) 

 ![alt текст](https://static.tildacdn.com/tild3364-3965-4237-b664-363533643431/Group_1321317003.svg)

