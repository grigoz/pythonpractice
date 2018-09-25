# 1
import pandas as pd
data = pd.read_csv('keywords.csv')
data.head()
geo_data = \
    {

    'Центр': ['москва', 'тула', 'ярославль'],

    'Северо-Запад': ['петербург', 'псков', 'мурманск'],

    'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']

     }
def regionss(row):
    if geo_data['Центр'][0] and geo_data['Центр'][1] and geo_data['Центр'][2] in row['keyword']:
        print('Центр')
    if geo_data['Северо-Запад'][0] and geo_data['Северо-Запад'][1] and geo_data['Северо-Запад'][2] in row['keyword']:
        print('Северо-Запад')
    if geo_data['Дальний Восток'][0] and geo_data['Дальний Восток'][1] and geo_data['Дальний Восток'][2] in row['keyword']:
        print('Дальний Восток')
    else:
        return 'undefined'

# 2
ratings = pd.read_csv('ml-latest-small/ratings.csv')
ratings.head()

def ratingss(row):
    if row['rating'] <= 2:
        return 'низкий рейтинг'
    if 2 < row['rating'] <= 4:
        return 'средний рейтинг'
    if row['rating'] == 4.5 and row['rating'] == 4.5:
        return 'высокий рейтинг'

ratings['class'] = ratings.apply(ratingss, axis=1)

# 3
from datetime import datetime
ratings_count = ratings.groupby('userId').count().reset_index()[['userId', 'movieId']]
film_fans_ratings_count = ratings_count[ratings_count['movieId'] >= 100]
film_fans_user_ids = film_fans_ratings_count['userId'].tolist()
fans_data = ratings[ratings['userId'].isin(film_fans_user_ids)]

time = fans_data.groupby('userId').agg(['min', 'max'])['timestamp']
time['min'] = pd.to_datetime(time['min'], unit='s')
time['max'] = pd.to_datetime(time['max'], unit='s')
time = time['max'] - time['min']
print(time)
