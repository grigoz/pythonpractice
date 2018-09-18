# 1
import numpy as np

def numpy_array(n):
    x = np.linspace(n-1, 0, n, dtype = int)
    return x

# 2
def numpy_diag(n):
    x = np.diag(np.linspace(n-1, 0, n, dtype = int), k=0)
    x.sum()
    return x, x.sum()

# 3
data3 = pd.read_csv('ratings.csv')
best_rating = data3[data3['rating'] == 5.0].sort_values(by='movieId', ascending=[False]).head(10)
best_rating['movieId'].value_counts().keys()[0]

# 4
filtered_countries = data[((data['country'] == 'Latvia') | (data['country'] == 'Estonia') | (data['country'] == 'Lithuania')) & ((data['category'] == 4) | (data['category'] == 12) | (data['category'] == 21)) & ((data['year'] == 2005) | (data['year'] == 2006) | (data['year'] == 2007) | (data['year'] == 2008) | (data['year'] == 2009) | (data['year'] == 2010)) & (data['quantity'] > 0)]
filtered_countries['quantity'].sum()


# 5
from numpy import linalg
a = np.array([[4, 2, 1], [1, 3, 0], [5, 4, 0]])
b = np.array([4, 12, -3])
linalg.solve(a, b)
