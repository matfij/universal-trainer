import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

np.random.seed(101)
mat = np.random.randint(1, 101, (100, 5))

plt.imshow(mat, aspect=0.1)
plt.colorbar()
plt.title('Image plot')

df = pd.DataFrame(data=mat)
print(df.describe())

df.plot(x=0, y=1, kind='scatter')

mat_scaled = MinMaxScaler().fit_transform(mat)

df.columns = ['f1', 'f2', 'f3', 'f4', 'y']
print(df.head())

x = df[['f1', 'f2', 'f3', 'f4']]
y = df['y']

x_tr, x_te, y_tr, y_te = train_test_split(x, y, test_size=0.45)
print(x_tr.shape, x_te.shape)

plt.show()
