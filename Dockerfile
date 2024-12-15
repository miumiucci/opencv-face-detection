# Базовый образ Python
FROM python:3.10-slim


# Установка зависимостей для работы с OpenCV
RUN apt-get update && apt-get install -y \
    libopencv-dev \
    && rm -rf /var/lib/apt/lists/*

# Установка библиотеки OpenCV
RUN pip install opencv-python

# Копируем приложение и изображение в контейнерс
COPY main.py /app/main.py
COPY samplee.jpg /app/samplee.jpg

# Устанавливаем рабочую директорию.
WORKDIR /app

# Команда для запуска приложения
CMD ["python", "main.py"]
