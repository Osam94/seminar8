import pandas as pd
import random

# Генерация данных
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# One hot encoding без get_dummies
data_one_hot = pd.DataFrame()
data_one_hot['robot'] = data['whoAmI'].apply(lambda x: 1 if x == 'robot' else 0)
data_one_hot['human'] = data['whoAmI'].apply(lambda x: 1 if x == 'human' else 0)

print(data)
print(data_one_hot.head())