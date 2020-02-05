# django_api

Тестовое задание

В тестовом задании нужно сделать API и интеграцию с сервисом ВК(авторизоваться через него).

Технические требования
    • Django 2+
    • Django Rest Framework 3.8+
    • PostgreSQL 9.6+
    • Python 3.6+
    • Для HTTP запросов можно использовать любую библиотеку, например requests
1. Добавить модель Profile c полями:
    • vk_id 
    • first_name
    • last_name
    • access_token                                 
2. Написать два endpoint-a для авторизации через вк, прочитать про это можно тут — https://vk.com/dev/authcode_flow_user, с токеном пользователя получить данные о пользователе с помощью метода users.get (https://vk.com/dev/users.get)  и сохранить нужные поля в таблицу Profile(vk_id должен быть уникален).
Пример endpoint`ов:
    • /api/get_code/ Получение code .
    • /api/token/ Получение access_token.
3. Написать сериализатор для модели Profile (Serializer в Django Rest Framework).
4.Сделать 2 endpoint`a которые будут возвращать данные из таблицы Profile.
Например:
    • /api/profiles/ - все записи
    • /api/profiles/1/ - только запись c id — 1
5. Загрузить код на GitHub.