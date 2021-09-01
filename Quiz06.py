
#Read csv file
import pandas as pd
df = pd.read_csv("Salaries.csv",header=0)

#Quiz 1
df.head(10)
df.head(20)
df.head(50)
df.tail(1)

#13 exercises in PPT (page.50 - 61)

#Check a particular column type
df['salary'].dtype
#Check types for all the columns
df.dtypes
#Selecting a column
df['sex']
df.sex

#Group data using rank
df_rank = df.groupby(['rank'])
#Calculate mean value for each numeric column per each group
df_rank.mean()
#Calculate mean salary for each professor rank:
df.groupby('rank')[['salary']].mean()
#Calculate mean salary for each professor rank:
df.groupby(['rank'], sort=False)[['salary']].mean()
#Calculate mean salary for each professor rank:
df_sub = df[ df['salary'] > 120000 ]
#Select only those rows that contain female professors:
df_f = df[ df['sex'] == 'Female' ]
#Select column salary:
df['salary']
#Select column salary:
df[['rank','salary']]
#Select rows by their position:
df[10:20]
#Select rows by their labels:
df_sub.loc[10:20,['rank','sex','salary']]
#Select rows by their labels:
df_sub.iloc[10:20,[0, 3, 4, 5]]
# Create a new data frame from the original sorted by the column Salary
df_sorted = df.sort_values( by ='service')
df_sorted.head()
df_sorted = df.sort_values( by =['service', 'salary'], ascending = [True, False])
df_sorted.head(10)



