import requests

url = 'https://myexport.exportcenter.ru/events/'

response = requests.get(url)

if 'Введите пароль' in response.text:
    print('Сайт требует аутентификации.')
elif 'капча' in response.text.lower():
    print('Сайт содержит капчу или антиспам-защиту.')
else:
    print('Сайт не требует аутентификации или капчи.')
