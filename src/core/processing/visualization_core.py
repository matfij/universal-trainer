import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# series
x = np.arange(0, 2, 0.1)
y = x**2
z = np.log(1+x)

plt.plot(x, y, 'r--')
plt.plot(x, z, 'bo')

plt.title('X vs Y vs Z')
plt.xlabel('time')
plt.ylabel('value')

plt.show()

# images
img = np.random.randint(0, 100, 10000).reshape(100, 100)

plt.imshow(img, 'rainbow')
plt.show()

# pandas visualization
df = pd.read_csv('src\core\data\salaries.csv')

df.plot(x='Age', y='Salary', kind='scatter')
plt.show()
