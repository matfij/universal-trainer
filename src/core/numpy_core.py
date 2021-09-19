import numpy as np

lst = [1, 2, 3]
arr = np.array(lst)

# creats array
arr = np.arange(0, 10, 0.1)
print(arr)

# creates empty arrays of zeros/ones
zrs = np.zeros((3, 5))
ons = np.ones((3, 5))
print(zrs)

# cretes evenly spaced array
ls = np.linspace(0, 22, 5)
print(ls)

# random int (array) in range
rarr = np.random.randint(0, 10, (4, 4))
print(rarr)

# seeded random numbers
np.random.seed(101)
rarr = np.random.randint(0, 100, 10)
print(rarr)

# array operations
mx = rarr.max()
mn = rarr.mean()
mxi = rarr.argmin()  # index of minimum value

# reshaping - sizes must match
rarr = rarr.reshape(2, 5)
print(rarr)
print(np.arange(0, 20).reshape(4, 5))

# accessing values
print(rarr[1, 4])
print(rarr[0:2, 1:4])

# masking - bool operations
print(rarr[rarr > 50])
