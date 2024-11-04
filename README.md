
Бэкенд-часть SPA веб-приложения **HABITS**

В книге хороший пример привычки описывается как конкретное действие, которое можно уложить в одно предложение:

я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]

За каждую полезную привычку необходимо себя вознаграждать или сразу после делать приятную привычку. Но при этом привычка не должна расходовать на выполнение больше двух минут.

*Model Habit:*

*owner* — создатель привычки.

*place* — место, в котором необходимо выполнять привычку.

*time* — время, когда необходимо выполнять привычку.

*action* — действие, которое представляет собой привычка.

*nice_habit* — привычка, которую можно привязать к выполнению полезной привычки.

*related_habit* — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных.

*period* (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.

*award* — чем пользователь должен себя вознаградить после выполнения.

*duration* — время, которое предположительно потратит пользователь на выполнение привычки.

*is_published* — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки.

*created_at* - дата создания привычки.

*Чем отличается полезная привычка от приятной и связанной?*

Полезная привычка — это само действие, которое пользователь будет совершать и получать за его выполнение определенное вознаграждение (приятная привычка или любое другое вознаграждение).
Приятная привычка — это способ вознаградить себя за выполнение полезной привычки. Приятная привычка указывается в качестве связанной для полезной привычки (в поле «Связанная привычка»).
Например: в качестве полезной привычки вы будете выходить на прогулку вокруг квартала сразу же после ужина. Вашим вознаграждением за это будет приятная привычка — принять ванну с пеной. То есть такая полезная привычка будет иметь связанную привычку.
Рассмотрим другой пример: полезная привычка — «я буду не опаздывать на еженедельную встречу с друзьями в ресторан». В качестве вознаграждения вы заказываете себе десерт. В таком случае полезная привычка имеет вознаграждение, но не приятную привычку.
Признак приятной привычки — булево поле, которые указывает на то, что привычка является приятной, а не полезной.

*Валидаторы*

* Исключен одновременный выбор связанной привычки и указания вознаграждения.
* Время выполнения должно быть не больше 120 секунд.
* В связанные привычки могут попадать только привычки с признаком приятной привычки.
* У приятной привычки не может быть вознаграждения или связанной привычки.
* Нельзя выполнять привычку реже, чем 1 раз в 7 дней.

*Пагинация*

Для вывода списка привычек реализована пагинацию с выводом по 5 привычек на страницу.

*Права доступа*

Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.
Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.

*Эндпоинты*

* Регистрация.
* Авторизация.
* Список привычек текущего пользователя с пагинацией.
* Список публичных привычек.
* Создание привычки.
* Редактирование привычки.
* Удаление привычки.

*Интеграция*

Сервис интегрирован с мессенджером Телеграм, который будет заниматься рассылкой уведомлений о необходимости выполнить привычку. За это отвечает функция *send_reminder_tg()*.

*Безопасность*

Для проекта настроиен CORS.

*Документация*

Настроен вывод документации через redok или swagger.

**Инструкция для запуска проекта**

Клонируйте данный репозиторий к себе на локальную машину:
    git clone https://github.com/valyaplotnikova/Habits.git

В файле .env_example подставьте свои переменные окружения и переименуйте файл в .env

Запустите Docker

Введите команду в терминале(выполнение команды осуществляется из папки проекта):

Для Compose V1:
```python
docker-compose up -d --build 
```
Для Compose V2:
```python
docker compose up -d --build 
```
