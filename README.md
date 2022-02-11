API_Final_Yatube

REST API для социальной сети блогеров Yatube, созданной в рамках учебного курса Яндекс.Практикум

Аутентификация по JWT-токену

Работает со всеми модулями социальной сети Yatube: постами, комментариями, группами, подписчиками

Поддерживает методы GET, POST, PUT, PATCH, DELETE

Предоставляет данные в формате JSON  
Стек технологий

#### _проект написан на Python с использованием Django REST Framework_
#### _библиотека Simple JWT - работа с JWT-токеном_
#### _система управления версиями - git_

Как запустить проект:

#### _Клонируйте репозитроий с проектом:_

######   _git clone https://github.com/valnem12/api_final_yatube_

#### _В созданной директории установите виртуальное окружение, активируйте его и установите необходимые зависимости:_

###### _python3 -m venv venv_

###### _. venv/bin/activate_

###### _pip install -r requirements.txt_

### _Выполните миграции:_

###### _python manage.py migrate_

#### _Создайте суперпользователя:_

###### _python manage.py createsuperuser_

#### _Запустите сервер:_

###### _python manage.py runserver_

Ваш проект запустился на http://127.0.0.1:8000/

Полная документация (redoc.yaml) доступна по адресу http://localhost:8000/redoc/

С помощью команды pytest вы можете запустить тесты и проверить работу модулей
Аутентификация

Выполните POST-запрос http://127.0.0.1:8000/api/v1/users/ передав поля username и password.

API вернет JWT-токен в формате:

{
    "refresh": "ХХХХХХХХХХХ",
    "access": "ХХХХХХХХХХХХ"
}

Токен вернётся в поле access, а данные из поля refresh нужны для обновления токена

При отправке запроcов передавайте токен в заголовке Authorization: Bearer <токен>
Как работает API_Yatube
Пример http-запроса (POST) для создания поста:

url = 'http://127.0.0.1/api/v1/posts/'
data = {'text': 'Your post'}
headers = {'Authorization': 'Bearer your_token'}
request = requests.post(url, data=data, headers=headers)

Ответ API_Yatube:

Статус- код 200

{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2020-08-20T14:15:22Z"
}

Пример http-запроса (GET) для получения списка подписчиков:

url = 'http://127.0.0.1:8000/api/v1/follow/'
headers = {'Authorization': 'Bearer your_token'}
request = requests.get(api, headers=headers)

Ответ API_Yatube:

Статус- код 200

[
  {
    "user": "string",
    "following": "string"
  }
]

