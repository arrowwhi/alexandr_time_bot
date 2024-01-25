# Используем базовый образ Python
FROM python:3.11

# Устанавливаем рабочую директорию в /app
WORKDIR /app

# Копируем все файлы из директории src в текущую директорию (/app)
COPY src/ .

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

CMD python main.py
