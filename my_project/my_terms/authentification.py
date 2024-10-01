# Авторизация и Аунтентификация

# Session-Based authentificatiion - аутентификация на основе сессий и cookies (встроенный в django_rest)
# Token-Base authentificatiion - аутентификация на основе токенов (установка библиотеки Djoiser)
# Json Web Token (JWT) authentification - аутентификация на основе JWT-токенов (установка библиотеки Simple JWT)
# Django Rest Framework OAuth - авторизация через социальные сети (нужно скачивать отдельно)

# Авторизация - проверка подлиности (наличия ) пользователя по введеным данным с данными, которые находяться в базе данных.
# Существует ли такой пользователь в нашой базе данных

# Аунтентификация - разрешение для пользователя на доступ к закрытой части сайта. Выполняеться после аутентификации


# 1) Session-Based Authorization (базовая авторизация пользователя)
# - пользователь отправляет данные в поле login и password.
# Если данные верный, тогда создаеться сессия для пользователя в базе данных нашего сервера.
# Создаеться уникальные значения session_id и user_id в базе данных. И ети данные отправляються в браузер
# Значение session_id сохраняеться в cookies браузера, толлько уже под названием cookies пользователя


# Session-Based Authentification (базовая аутентификация пользователя)
# - браузер отправляет cookies пользователя, он же session_id на сервера
# И если в базе данных сервера нашего сайта есть такое значение session_id, тогда аутентификация пользователя прошла успешно
# Изменяться session_id, если пользователь выйдет из системы. session_id удаляеться из базы данных сервера нашего сайта
# И при новой попытке пользователя пройти аутентификация создастся новый session_id и user_id в базе данных сервера нашего сайта
# Проблема в том, что пользователь жестко привязан к одному устройству на котором зашел на сайт

# -------------------------------------------------------------------------------------------------------------------------------------------------------

# 2) Token-Based Authentificatiion (аутентификация по токенам)
# Токен - специальный ключ аутентификации пользователя
# Нужно указывать токен в заголовке запроса
# Пользователь может заходить с разных устройст на один сайто по одному указаному токену
# Можно реализовать двумя способами
#  - обычная аутентифкация токанеми библиотеки Djoser
#  - аутентифкация по JWT-токенам библиотеки Simple JWT

# Клиент -> Форма Входа -> Пользователь Регистрируеться в базе -> Пользователь Получат Номер Свого Токена ->
# -> Клиент Хранит где-то локально номер токера -> При входае на сайт отправляет на сайта номер своего токена для входа.

# Ети токены нужны для того, чтоб пользователь мог заходить с разных устройств в свою учетную запись на одном сайте одновременно

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# 3) Json Web Token (JWT) authentification - аутентификация на основе JWT-токенов
# JWT токены - ето большой набор символов, который сосоит из трех частей -> header , payload , signature
# Header    - json-строка, которая содержит информацию аоб алгоритме шифрования токенов
# Payload   - json-строка, которая содержит информацию о пользователе (username , password, email), которому генерируем JWT-токен
# Signature - берет данные из Header и Payload и шифрует их с помощью SECRET_KEY нашего проекта

# JWT Token -> header.payload.signature

# Ети JWT-токены нужны для того, чтоб пользователь мог одной учетной записью взаемодействовал с множеством независимых сайтов или приложений
# Ето например сервисы, сайты под руководством Google

# Сервер Авторизации(центр независимых сервисов,сайтов) отправляет ответ на зпарос пользоватея два токена -> access_token и refresh_token
# access_token   - етот токен используеться пользоватеелм в момент входа одной учетной записью в другие сервисы,сайты (токен храниться 5 минут)
# refresh_token  - етот токен нужен для создания новый access_token после прохождения 5 минут и нового себя refresh_token (время жизни refresh_token одни сутки)
