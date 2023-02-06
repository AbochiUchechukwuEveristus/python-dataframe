# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 16:28:52 2023

@author: ABOCHI
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

marvel_data = [
    ['Spider-Man', 'male', 1962],
    ['Captain America', 'male', 1941],
    ['Wolverine', 'male', 1974],
    ['Iron Man', 'male', 1963],
    ['Thor', 'male', 1963],
    ['Thing', 'male', 1961],
    ['Mister Fantastic', 'male', 1961],
    ['Hulk', 'male', 1962],
    ['Beast', 'male', 1963],
    ['Invisible Woman', 'female', 1961],
    ['Storm', 'female', 1975],
    ['Namor', 'male', 1939],
    ['Hawkeye', 'male', 1964],
    ['Daredevil', 'male', 1964],
    ['Doctor Strange', 'male', 1963],
    ['Hank Pym', 'male', 1962],
    ['Scarlet Witch', 'female', 1964],
    ['Wasp', 'female', 1963],
    ['Black Widow', 'female', 1964],
    ['Vision', 'male', 1968]
]

### Create a `marvel_df` pandas DataFrame with the given marvel data
df = pd.DataFrame(marvel_data)

### Add column names to the `marvel_df`
df['name'] = df[0]
df['sex'] = df[1]
df['first_appearance'] = df[2]

### Drop the name column as it's now the index
df = df.drop([0, 1, 2], axis=1)

### Add index names to the `marvel_df` (use the character name as index)
df = df.set_index('name')

### Drop 'Namor' and 'Hank Pym' rows
df.drop(index = ['Namor', 'Hank Pym'], inplace=True)

### Show the first 5 elements on `marvel_df`
print(df.head(5))

### Show the last 5 elements on `marvel_df`
print(df.tail(5))

### Show just the sex of the first 5 elements on `marvel_df`
print(df.sex.head(5))

### Show the first_appearance of all middle elements on `marvel_df` 
print(df.sex)

### Show the first and last elements on `marvel_df`
print(df.head(1), df.tail(1))

### Modify the `first_appearance` of 'Vision' to year 1964
df.at['Vision', 'first_appearance'] = 1964

### Add a new column to `marvel_df` called 'years_since' with the years since `first_appearance`
df['years_since'] = 2023 - df['first_appearance']

### Given the `marvel_df` pandas DataFrame, make a mask showing the female characters
mask = df['sex'] == 'female'
print('mask')

### Given the `marvel_df` pandas DataFrame, get the male characters
males = df[df['sex'] == 'male']
print(males)

### Given the `marvel_df` pandas DataFrame, get the characters with `first_appearance` after 1970
after1970 = df[df['first_appearance'] > 1970]
print(after1970)

### Given the `marvel_df` pandas DataFrame, get the female characters with `first_appearance` after 1970
femaleafter1970 = df[(df['sex'] == 'female') & (df['first_appearance'] > 1970)]
print(femaleafter1970)

### Show basic statistics of `marvel_df`
df.describe()
df.info()

### Given the `marvel_df` pandas DataFrame, show the mean value of `first_appearance`
mean_first = df['first_appearance'].mean()
print(mean_first)

### Given the `marvel_df` pandas DataFrame, show the min value of `first_appearance`
min_first = df['first_appearance'].min()
print(min_first)

### Given the `marvel_df` pandas DataFrame, get the characters with the min value of `first_appearance`
min_character = df[df['first_appearance'] == min_first]
print(min_character)

### Reset index names of `marvel_df`
df = df.reset_index()

### Plot the values of `first_appearance`
plt.plot(df['first_appearance'])

# Plot a histogram (plot.hist) with values of `first_appearance`
df['first_appearance'].plot.hist(color = 'blue', edgecolor = 'red')
plt.xlabel('year')
plt.ylabel('frequency')
plt.title('Histogram of First Appearance')
plt.show()



