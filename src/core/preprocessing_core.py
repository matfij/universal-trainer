import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

data = np.random.randint(0, 100, (10, 2))
print(data)

# normalize numeric values
scaler = MinMaxScaler()
scaler.fit(data)

arr = np.random.randint(0, 100, (50, 4))
df = pd.DataFrame(data=arr, columns=['f1', 'f2', 'f3', 'y'])

# split training and testing sets
x = df[['f1', 'f2', 'f3']]
y = df['y']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=101)
print(x_train.shape, x_test.shape)
