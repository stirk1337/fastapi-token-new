# Fastapi-token

## Запуск без docker-compose

Установите менеджер зависимостей Poetry

```console
foo@bar:~$ whoami
foo
```

Установите зависимости

---bash
poetry install
---

Запустите базу данных PostgreSQL 15 и настройте коннект в файле .env.
(Я знаю что пушить файлы .env нельзя, сделал это для удобства проверки)

Перейдите в директорию src

---bash
cd src
---

Запустите приложение

---bash
poetry run uvicorn main:app
---

Приложение будет доступно на http://127.0.0.1:8000/

## Запуск с docker-compose

Установите Docker (инструкция не прилагается)

Запустите приложение 

---bash
docker-compose up
---

Приложение будет доступно на http://127.0.0.1:8000/
