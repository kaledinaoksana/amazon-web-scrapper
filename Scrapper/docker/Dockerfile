# Используйте базовый образ Python
FROM python:3.8

# Установка рабочей директории внутри контейнера
WORKDIR /Scrapper

# Копирование зависимостей проекта
COPY requirements.txt .

# Установка зависимостей
RUN conda install --file requirements.txt

# Копирование файлов проекта в контейнер
COPY . .

# Команда, которая будет выполнена при запуске контейнера
CMD [ "python", "amazon_bot.py" ]
