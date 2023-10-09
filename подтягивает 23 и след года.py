import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

# Множество для отслеживания посещенных страниц
visited_pages = set()

# Функция для поиска ключевых слов на странице
def search_keywords_on_page(page_url, keywords):
    # Проверяем, посещали ли мы уже эту страницу
    if page_url in visited_pages:
        return

    # Добавляем текущую страницу в множество посещенных
    visited_pages.add(page_url)

    # Отправляем GET-запрос к странице
    response = requests.get(page_url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Получаем HTML-код страницы
        page_content = response.text

        # Инициализируем объект BeautifulSoup для парсинга
        soup = BeautifulSoup(page_content, 'html.parser')

        # Используем регулярное выражение для разделения текста на предложения
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', soup.get_text())

        # Поиск ключевых слов на странице и их окружения
        # Поиск ключевых слов на странице и их окружения
        for keyword in keywords:
            for sentence in sentences:
                # Use re.IGNORECASE to perform a case-insensitive search
                if re.search(rf'\b{re.escape(keyword)}\b', sentence, re.IGNORECASE):
                    # Выводим текущее предложение
                    print(f'Ключевое слово "{keyword}" найдено на странице {page_url}:')
                    print(sentence.strip())

        # Поиск ссылок на другие страницы и рекурсивный вызов функции для них
        links = soup.find_all('a', href=True)
        for link in links:
            absolute_url = urljoin(page_url, link['href'])
            search_keywords_on_page(absolute_url, keywords)

    else:
        print(f'Ошибка при отправке запроса к странице {page_url}.')

# URL сайта, который вы хотите парсить
base_url = 'https://myexport.exportcenter.ru/events/'

# Ключевые слова, которые вы ищете на сайте
keywords = ['оаэ', 'арабские эмираты', 'саудовская аравия', '\bоман\b', 'бахрейн',
    'катар', 'кувейт', 'египет', 'алжир', 'кения', 'танзания', 'эфиопия',
    'нигерия', 'уганда', 'ливия', 'иран', 'пакистан', 'индия',
    'ОАЭ', 'АРАБСКИЕ ЭМИРАТЫ', 'САУДОВСКАЯ АРАВИЯ', 'ОМАН', 'БАХРЕЙН',
    'КАТАР', 'КУВЕЙТ', 'ЕГИПЕТ', 'АЛЖИР', 'КЕНИЯ', 'ТАНЗАНИЯ', 'ЭФИОПИЯ',
    'НИГЕРИЯ', 'УГАНДА', 'ЛИВИЯ', 'ИРАН', 'ПАКИСТАН', 'ИНДИЯ',
    'Оаэ', 'Арабские эмираты', 'Саудовская аравия', 'Оман', 'Бахрейн',
    'Катар', 'Кувейт', 'Египет', 'Алжир', 'Кения', 'Танзания', 'Эфиопия',
    'Нигерия', 'Уганда', 'Ливия', 'Иран', 'Пакистан', 'Индия']

# Начинаем поиск на главной странице
search_keywords_on_page(base_url, keywords)
