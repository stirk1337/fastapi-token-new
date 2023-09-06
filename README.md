# Fastapi-token

## Запуск без docker-compose

Установите зависимости

```console
root@stirk1337:~$ pip install -r requirements.txt
```

Запустите базу данных PostgreSQL 15 и настройте коннект в файле .env

Перейдите в директорию src

```console
root@stirk1337:~$ cd src
```

Запустите приложение

```console
root@stirk1337:~$ python3 main.py
```

Приложение будет доступно на http://127.0.0.1:8000/

## Запуск с docker-compose

Установите Docker (инструкция не прилагается)

Запустите приложение 

```console
root@stirk1337:~$ docker-compose up
```

Приложение будет доступно на http://127.0.0.1:8000/

## Документация

После запуска вся документация будет доступна на http://127.0.0.1:8000/docs

## Тесты

Для запуска тестов вам нужно настроить коннект к тестовой базе данных PostgreSQL 15 в файле .env.

Запуск тестов

```console
root@stirk1337:~$ pytest tests
```
