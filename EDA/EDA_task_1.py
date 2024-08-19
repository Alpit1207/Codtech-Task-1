# import the required libraries

import pandas as pd
import numpy as np
import seaborn as sns                       # For visualisation
import matplotlib.pyplot as plt             # For visualisation
# %matplotlib inline     
sns.set(color_codes=True)

# Read the data set

df = pd.read_csv("C:/Users/alpit/OneDrive/Desktop/Codtech/EDA/data/data.csv")
df = pd.DataFrame(df)
# show top 5 rows

print(df.head(5))

# show last 5 rows

print(df.tail(5))

# check data types and typecast if required

print(df.dtypes)

# drop the irrelevant columns that we will never use

df = df.drop(["Number of Doors","Market Category","Vehicle Size","Popularity"],axis=1)

print(df.head(5))
print(df.dtypes)

# to increase the readability we change the name of the column

df = df.rename({"Engine Fuel Type":"Fuel type","Engine HP":"HP","Engine Cylinders":"Cylinders","Driven_Wheels":"Drive Mode","MSRP":"Price","Vehicle Style":"Style","Make":"Brand"}, axis=1)
print(df.dtypes)

# remove the duplicate rows from the data set

duplicate_df = df.duplicated().sum()
print(duplicate_df)

df = df.drop_duplicates()
print(df.duplicated().sum())

# now data set has 0 duplicate rows

print(df.count())

# drop the missing values

null_df = df.isnull().sum()
print(null_df)

df = df.dropna()  # all the null values are removed
print(df.count())

null_df = df.isnull().sum()
print(null_df)

# detect outliers :- those values that stand out from all values

# use box plot to do so

box_plot = sns.boxplot(x=df['Price'])
plt.show()

box_plot = sns.boxplot(x=df['HP'])
plt.show()

box_plot = sns.boxplot(x=df['HP'])
plt.show()

box_plot = sns.boxplot(x=df['Fuel type'])
plt.show()


Q1 = df.Price.quantile(0.25)
Q3 = df.Price.quantile(0.75)
IQR = Q3-Q1
print(IQR)

lower_bound_value = Q1 - (1.5 * IQR)
upper_bound_value = Q3 + (1.5 * IQR)
print(lower_bound_value )
print(upper_bound_value)

print(df['Price'] > upper_bound_value)
print(df['Price'] < lower_bound_value)

df = df[df['Price'] < upper_bound_value ]
df = df[df['Price'] > lower_bound_value]

print(df.shape)



# to check which company has highest number of car we use histogram

Brand_count = df.Brand.value_counts()
print("Printing Values")
Brand_count.plot(kind="bar",figsize=(10,5) , orientation = 'vertical' )
plt.title("Number of cars by Brand")
plt.ylabel('Number of cars')
plt.xlabel('Brand')
plt.show()

#  to find the relationship between the features we use heat map

# Select only numeric columns
numeric_df = df.select_dtypes(include=['int64','float64'])

# Calculate the correlation matrix
corr = numeric_df.corr()
print(corr)
plt.figure(figsize=(10, 5))
sns.heatmap(data=corr, cmap="crest", annot=True)
plt.show()

# creating a pie chart to see the top 10 brand by sale

top_brand = df.Brand.value_counts().nlargest(10)
print(top_brand)
top_brand.plot(kind = 'pie')
plt.show()

