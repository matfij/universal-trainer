import pandas as pd

# reading files
df = pd.read_csv('src\core\data\salaries.csv')
print(df.describe())

# accessing columns
print(df[['Salary', 'Name']])
print(df['Salary'].max())

# filter values
print(df[df['Salary'] > 55000])

# to array
arr = df.values
print(arr)
