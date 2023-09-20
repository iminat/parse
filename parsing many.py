import requests
from bs4 import BeautifulSoup

# Список URL-адресов сайтов, которые вы хотите анализировать
urls = [
    'https://www.exportchel.ru/',
    'https://myexport.exportcenter.ru/events/',
    'https://kalugaexport.ru/',
    'https://bashexport.com/events-announcement/',
    'https://exportkirov.ru/meropriyatiya/'
]

# Ключевые слова, которые вы ищете на сайтах
keywords = ['оаэ', 'арабские эмираты', 'саудовская аравия', '\bоман\b', 'бахрейн',
    'катар', 'кувейт', 'египет', 'алжир', 'кения', 'танзания', 'эфиопия',
    'нигерия', 'уганда', 'ливия', 'иран', 'пакистан', 'индия',
    'ОАЭ', 'АРАБСКИЕ ЭМИРАТЫ', 'САУДОВСКАЯ АРАВИЯ', 'ОМАН', 'БАХРЕЙН',
    'КАТАР', 'КУВЕЙТ', 'ЕГИПЕТ', 'АЛЖИР', 'КЕНИЯ', 'ТАНЗАНИЯ', 'ЭФИОПИЯ',
    'НИГЕРИЯ', 'УГАНДА', 'ЛИВИЯ', 'ИРАН', 'ПАКИСТАН', 'ИНДИЯ',
    'Оаэ', 'Арабские эмираты', 'Саудовская аравия', 'Оман', 'Бахрейн',
    'Катар', 'Кувейт', 'Египет', 'Алжир', 'Кения', 'Танзания', 'Эфиопия',
    'Нигерия', 'Уганда', 'Ливия', 'Иран', 'Пакистан', 'Индия']

# Перебираем каждый URL-адрес
for url in urls:
    # Отправляем GET-запрос к сайту
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Получаем HTML-код страницы
        page_content = response.text

        # Инициализируем объект BeautifulSoup для парсинга
        soup = BeautifulSoup(page_content, 'html.parser')

        # Поиск ключевых слов на странице
        for keyword in keywords:
            # Находим все элементы, содержащие ключевое слово
            elements_with_keyword = soup.find_all(string=lambda text: keyword in text)

            # Выводим результаты
            if elements_with_keyword:
                print(f'Ключевое слово "{keyword}" найдено на сайте {url}:')
                for element in elements_with_keyword:
                    print(element.strip())
            else:
                print(f'Ключевое слово "{keyword}" не найдено на сайте {url}.')

    else:
        print(f'Ошибка при отправке запроса к сайту {url}.')
