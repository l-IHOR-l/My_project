import requests
import pprint

random_joke = requests.get('https://api.chucknorris.io/jokes/random').json()['value']
joke_category = requests.get('https://api.chucknorris.io/jokes/categories').json()


print(joke_category)

category_input = input('Вибери категорію для шутки: ')

if category_input in joke_category:
    print(requests.get(f'https://api.chucknorris.io/jokes/random?category={category_input}').json()['value'])
else:
    print('Неправильна введена категорія категорія')

