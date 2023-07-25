import requests
import pprint

random_joke = requests.get('https://api.chucknorris.io/jokes/random').json()['value']
joke_category = requests.get('https://api.chucknorris.io/jokes/categories').json()

[print(i) for i in joke_category]

categorie: str = input('cat: ')
if categorie in joke_category:
    print(requests.get(f'https://api.chucknorris.io/jokes/random?category={categorie}').json()['value'])
else:
    print('Missed')
