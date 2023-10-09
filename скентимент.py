from textblob import TextBlob

# Пример текста для анализа
text = "Этот продукт просто ужасен. Я ненавижу его."

# Создаем объект TextBlob
blob = TextBlob(text)

# Анализ сентимента
sentiment = blob.sentiment

# Выводим результаты
print("Результаты анализа сентимента:")
print(f"Текст: {text}")
print(f"Положительность: {sentiment.polarity}")
print(f"Отрицательность: {sentiment.subjectivity}")
