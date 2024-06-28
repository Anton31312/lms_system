## Запуск проекта с использованием Docker

### Шаги по запуску

1. **Клонируйте репозиторий**
    ```
    git clone https://github.com/Anton31312/lms_system.git
    ```

2. **Переименуйте пример файла окружения с .env.sample в .env и отредактируйте его**

    *Дополнительно* \
    *Если вы используете redis в качестве брокера celery, то в файле .env* \
    *В поле CACHES_LOCATION замените localhost(127.0.0.1) на redis*


4. **Постройте и запустите контейнеры Docker**
    ```
    docker-compose up -d --build
    ```

5. **Выполните миграции**

   ```
   docker-compose exec app python manage.py migrate
   ```

6. **Создание суперпользователя**
    ```
    docker-compose exec app python manage.py csu
    ```
    *Дополнительно* \
    Данные для входа под аккаунтом администратора: \
    *Логин: admin3@sky.pro* \
    *Пароль: 123qwe456rty* 

### Доступ к приложению
- Приложение будет доступно по адресу: [http://localhost:8000](http://localhost:8000)
- Админ панель Django: [http://localhost:8000/admin](http://localhost:8000/admin)

### Остановка контейнеров
Для остановки контейнеров используйте следующую команду:

```
docker-compose down
```
