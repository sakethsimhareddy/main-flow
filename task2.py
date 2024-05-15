
import pandas as pd

# Read a CSV file into a DataFrame
df = pd.read_csv(r"C:\Users\saket\Downloads\01.Data Cleaning and Preprocessing.csv")
df


# Display the first 5 rows of the DataFrame
print("First 5 rows of the DataFrame:")
print(df.head())

# Display the last 5 rows of the DataFrame
print("\nLast 5 rows of the DataFrame:")
print(df.tail())

# Display the number of rows and columns in the DataFrame
print("\nNumber of rows and columns in the DataFrame:", df.shape)

# Display the data types of the columns in the DataFrame
print("\nData types of the columns in the DataFrame:")
print(df.dtypes)


print("\nStatistical summary of the DataFrame:")
print(df.describe())


df = df.drop_duplicates()
df

df.isnull()

df.isnull().sum()

df.notnull()

df.isnull().sum().sum()

# Fill missing values with a specific value
df1=df.fillna(0)  # fill missing values with 0
df1

#Fill missing values with forward fill
df2=df.fillna(method='ffill')  # fill missing values with forward fill
df2

df3=df.fillna(method='bfill')  # fill missing values with backward fill
df3

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
df2.drop(['Observation'],axis=1,inplace=True)
df2.columns

Q1 = df2.quantile(0.25)
Q3 = df2.quantile(0.75)
IQR=Q3-Q1
print(IQR)

df2=df2[~((df2<(Q1-1.5*IQR))|(df2>(Q3+1.5*IQR))).any(axis=1)]
df2

print("\nStatistical summary of the DataFrame:")
print(df2.describe())

# Group the DataFrame by a column and calculate the mean
print("\nGroup the DataFrame by a column and calculate the mean:")
print(df2.groupby("ChipRate").mean())

# Sort the DataFrame by a column
print("\nSort the DataFrame by a column:")
print(df2.sort_values("ChipRate"))

df2[df2['ChipRate'] == 11.817]  # filter rows where column_name is equal to value
