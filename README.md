# Автоматизированное рабочее место сотрудника многофункционального центра предоставления государственных и муниципальных услуг

## Инструкция для запуска приложения

### Установка и настройка

#### 1. Скачайте или клонируйте репозиторий на свой компьютер;
##### git clone https://github.com/ZakharEliseev/proj_2
#### 2. Создайте виртуальное окружение Python с помощью команды `python -m venv venv`;
#### 3. Активируйте виртуальное окружение с помощью команды `source venv/bin/activate` на Linux или MacOS или `venv\Scripts\activate` на Windows;
#### 4. Установите необходимые зависимости с помощью команды `pip install -r requirements.txt`;
#### 5. Настройте базу данных SQLite3, используя команды:

##### `flask db init`; # создание репозитория миграций

##### `flask db migrate`; # генерация первой миграции

##### `flask db upgrade`.  # применить изменения описанные сценарием миграции, к базе данных
### Запуск приложения
#### 1. Перейдите в каталог вашего приложения;
#### 2. Настройте переменную `path` для доступа к `poppler-0.68.0\bin`:
#### используйте команду на Windows: `set path=%path%;C:\path\to\poppler-0.68.0\bin`
#### на Linux или MacOS: `export PATH=$PATH:/path/to/poppler-0.68.0/bin` 
#### 3. Запустите приложение с помощью команды `flask run`.

#### Приложение запустится по адресу  http://127.0.0.1:5000 в режиме отладки. 
