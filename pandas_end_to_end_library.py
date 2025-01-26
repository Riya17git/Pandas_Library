# -*- coding: utf-8 -*-
"""Pandas_End_To_End_Library.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1onD0GMpBMrqpG2532awdh-9AHVMo1YJs
"""

import pandas as pd

"""# Pandas"""



"""# There are two termenologies in pandas
1. Series
2. Dataframe

"""

## Series

## A series is like a one column in dataset.it is 1-D array holding any datatype



"""## Series from lists"""

# string object

country = ['India','pakistan','shrilanka','nepal']
pd.Series(country)

# int object

num = [34,56,33,56,21]
pd.Series(num)

subject = ['english','maths','hindi','sciencse']
marks = [34,56,33,56]

pd.Series(marks,index=subject)



"""# series from decitionary"""

marks = {'english':34,'maths':56,'hindi':33,'sciencse':56}
a = pd.Series(marks)
a



"""## read_csv method"""

df = pd.read_csv('/content/field_dataset.csv')
df.head()

"""## # with one col
subs = pd.read_csv('/content/subs.csv',squeeze=True)
subs
"""



"""## Series methods"""

df.head()

df.tail()

"""## sample() is useful when my data is sorted and i want to generate random rows"""

df.sample(5)

df.value_counts()

# sort_values --->
df.sort_values('y',ascending = False).head(1).values[0]

# sort index
df.sort_index(ascending=False)

## careful while using inplace function bcz it is permentaly making changes in data.

"""## series Maths method"""

df.count()

df['x'].sum()

df['x'].median()

df.min()



"""## series Indexing and slicing"""

df['x'][21]

df['y'][-1]  ## negative indexing will not work

df['x'][-5:]  # negative values will work in slicing

df['x'][[1,3,5,7]]



"""## series with python funcnalities"""

print(len(df))
print(type(df))
print(dir(df))

for i in df:
  print(i)



"""## Boolean indexing in series"""

df[df['x'] > 1].size

df[df['x']==1]

num_count = df['x'].value_counts()
num_count[num_count > 60]



"""## Plotting graph on series"""

df.plot()



"""## Dataframe

## Creating DataFrame
"""

# from list

student = [100,20,4],[200,34,5],[300,45,6]

pd.DataFrame(student,columns=['iq','mark','package'])

# using dictionary

student_dict = {'id':[100,200,300],'mark':
                [20,34,45],'package':
              [4,5,6]}

pd.DataFrame(student_dict)



"""## DataFrame arttributes and methods"""

# shape , dtypes , columns , describe , head , tail , sample , info , isnull , rename , duplicated



"""## Math functions"""

# sum , min , max , mean



"""## fetching columns from data

# This is for column
"""

# single column

# movies['movie_name']

# For fetching multiple columns we use fency indexing

# movies[['name','rating','actor']]



"""## fetching rows from data

# This is for row

#iloc ---> searches using index position
#loc ----> searches using index labels

through iloc we fetch using index number and loc we will fetch using lable (column name)
"""

# movies.iloc[0:5]  ----> will fetch 5 columns

# fency indexing  ---> you want 0, 4 ,5 ,9 columns

#movies.iloc[[0,4,5,9]]

# movies.loc['Actor']



"""## Filtering on IPL dataset"""

import pandas as pd

df1 = pd.read_csv('/content/batsman_runs_ipl.csv')
df1.head()

df1 = pd.read_csv('/content/ipl-matches.csv')
df1.head(3)

# find all the final winners

df1[df1['MatchNumber'] == 'Final'][['Season','WinningTeam']]

# how many super over finishes have occured?

df1[df1['SuperOver'] == 'Y'].shape[0]

df1[df1['SuperOver'] == 'Y']['SuperOver'].count()

df1.tail(5)

# how many matches has csk won in kolkata?

df1[(df1['City'] == 'Kolkata') & (df1['WinningTeam'] == 'Chennai Super Kings')]

# toss winnwe is match winner in percentage
a = df1[df1['TossWinner'] == df1['WinningTeam']].shape[0]

b = df1.shape[0]

r = round(a/b * 100)
print(r)

# i have genre column in dataset like action| drama| horror  and i want to fetch action from it.
# for that
# movies['genres'].str.split('|').apply(lambda x: 'Action' in x)

df1.info()

"""## How to change datatype and reduce the memory usage in data"""

df1['ID'] = df1['ID'].astype('int32')

df1.info()

df1['Team1'] = df1['Team1'].astype('category')

df1.info()

# between  I want to count matches of virat kohli where he has scored > 49 and < 99

# vk[vk.between(49,99)].size

# clip i want to clip the values between 100 and 200 means which values < 100 will become 100 ans > 200 become 200

# subs.clip(100,200)

df1.head(1)

df1 = df1.drop_duplicates()

df1.duplicated().sum()

# null values

df1.isnull().sum()

# drop null

df1.dropna()

df1.fillna(0)

df = pd.read_csv('/content/ipl-matches.csv')
df.head()

df['first name'] = df['Team1'].apply(lambda x:x.split()[0])

df.head(3)

"""## Apply function

when you want to scrape some data or information from column and make new column apply function will be used

## Copy function

when you are making changes in head and tail function this will also make changes to original data.

this is why we use copy to copy our data.

## Dataframe Methods
"""

# value_counts            # isnull               # corr
# sort_values             # dropna               # nlargest --> nsmallest
# rank                    # fillna               # insert
# sort index              # drop_suplicates      # copy
# set index               # drop
# rename index            # apply
# unique & nunique        # isin

import pandas as pd
import numpy as np

# value_counts (series and dataframe)

marks = pd.DataFrame([[100,80,90],
                     [45,67,89],
                     [65,98,76],
                     [87,67,54]],columns=['english','maths','hindi'])

marks.value_counts()

marks

df = pd.read_csv('/content/ipl-matches.csv')
df.head(2)

# find which player has won most man of the match award -> in final & semifinal

df[~df['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts()

# plot after toss team chose batting or fielding

df['TossDecision'].value_counts().plot(kind='pie')

# how many matches each team has played

(df['Team1'].value_counts() + df['Team2'].value_counts()).sort_values(ascending=False)

## Sort_values (Series & DataFrame)

## rank(only apply on series)

marks['english'].rank()

df.sort_index(ascending=False)

# set_index

df.set_index('ID')

# reset_index

df.reset_index()

df.set_index('ID')

# how to replace existing index without loosing previous index

df.reset_index().set_index('City')

# rename

df.rename(columns = {'City':'city'})

df.rename(index = {'Mumbai':'Bombay'})

# unique & nunique  (series)

df['Team1'].unique()

df['Team1'].nunique()

# isnull, notnull, hasnull (series & DataFrame)

# dropna --->  will remove all rows who ever has missing value in any of the column

# drop_dupicates

df['all_players'] = df['Team1Players'] + df['Team2Players']
df.head(2)

# find the last match played by virat kohli in delhi?

def is_virat_kohli(x):
  return 'V Kohli' in x

df['is_virat_kohli'] = df['all_players'].apply(is_virat_kohli)
df.head()

df[(df['City'] == 'Delhi') & (df['is_virat_kohli'] == True)].drop_duplicates(subset=['City','is_virat_kohli'],keep='first')

# apply function

"""## Group By function"""

import pandas as pd
import numpy as np

df = pd.read_csv('/content/imdb-top-1000.csv')
df.head(2)

genre = df.groupby('Genre')

rating_std = genre['IMDB_Rating'].std()
print(rating_std)

# Q : find top 3 genres by total earnings

g = df.groupby('Genre')['Gross'].sum().sort_values(ascending=False).head(3)
print(g)

# Q : find top 3 genres by imdb rating

g1 = df.groupby('Genre').mean('IMDB_Rating')['IMDB_Rating'].sort_values(ascending=False).head(3)
print(g1)

# Q find the director with most popularity based on number of votes

g2 = df.groupby('Director')['No_of_Votes'].sum().sort_values(ascending=False).head(1)
print(g2)

# Q find the highest rated movie of each genre

g3 = df.groupby('Genre')['IMDB_Rating'].max()
print(g3)

# find the number of movies done by each actor

#df['Star1'].value_counts()  --- what if you are not allowed to use value_count?

df.groupby('Star1')['Series_Title'].count().sort_values(ascending=False)

# GroupBy Attributes and Methods
# find total number of groups -> len
# find items in each group -> size
# first()/last() -> nth item
# get_group -> vs filtering
# groups
# describe
# sample
# nunique

genre = df.groupby('Genre')

genre.get_group('Fantasy')

genre.nunique()

g1  = genre.agg(
    {
        'Runtime':'mean',
        'IMDB_Rating':'mean',
        'No_of_Votes':'sum',
        'Metascore':'min'
    }
)

genre.agg(['min','max','sum'])

genre.agg(
    {
        'Runtime':['min','mean'],
        'IMDB_Rating':'mean',
        'No_of_Votes':['sum','max'],
        'Gross':'sum',
        'Metascore':'min'
    }
)

# Q: find highest rated movie of each genre.

df = pd.DataFrame(columns=df.columns)
dfs = []
for group,data in genre:
  dfs.append(data[data['IMDB_Rating'] == data['IMDB_Rating'].max()])

df = pd.concat(dfs, ignore_index=True)
df

# find number of movies starting with A in each group

def find(group):
  return group['Series_Title'].str.startswith('A').sum()

genre.apply(find)

# find ranking of each movie according to there imdb rating

def rank_movie(data):
  data['movie_rank'] = data['IMDB_Rating'].rank(ascending=False)
  return data

genre.apply(rank_movie)

# find normalize imdb rating group wise

def norm(data):
  data['Normalize_rating'] = data['IMDB_Rating'] - data['IMDB_Rating'].min() / data['IMDB_Rating'].max() - data['IMDB_Rating'].min()
  return data

genre.apply(norm)

"""## Group by on multiple columns"""

duo = df.groupby(['Director','Star1'])
duo

duo.size()

# find the most earning actor director combo

duo['Gross'].sum().sort_values(ascending=False)

# find the best actor , genre combo interms of metascore

df.groupby(['Star1','Genre'])['Metascore'].mean().reset_index().sort_values('Metascore')

ipl = pd.read_csv('/content/deliveries (1).csv')
ipl.head(2)

"""## If you want to convert a series into dataframe apply reset_index()"""

# find top 10 batsman in terms of runs

ipl.groupby('batsman')['total_runs'].sum().reset_index().sort_values('total_runs',ascending=False).head(10)

ipl.columns

# find batsman with max number of sixes

six = ipl[ipl['batsman_runs']==6]

six.groupby('batsman')['batsman'].count().sort_values(ascending = False).head()

# find the batsman with most 4s and 6s in last five overs

ipl[(ipl['over']> 15)  & (ipl['batsman_runs'] == 6) | (ipl['batsman_runs'] == 4)].groupby('batsman')['batsman_runs'].count().sort_values(ascending=False).head(1)

# find v kohli record again all teams

ipl[ipl['batsman'] == 'V Kohli'].groupby('bowling_team')['batsman_runs'].sum().sort_values(ascending=False)

# write a function which return highest score of any batsman

def highest(name):
  temp_df = ipl[ipl['batsman'] == name]
  return temp_df.groupby('match_id')['batsman_runs'].sum().sort_values(ascending=False).head(1)

print(highest('V Kohli'))

"""## Merging , Joining and Concatinating"""

import pandas as pd
import numpy as np

courses = pd.read_csv('/content/courses.csv')
students = pd.read_csv('/content/students.csv')
nov = pd.read_csv('/content/reg-month1.csv')
dec = pd.read_csv('/content/reg-month2.csv')

matches = pd.read_csv('/content/matches.csv')
delivery = pd.read_csv('/content/deliveries (2).csv')

# concat

pd.concat([nov,dec],ignore_index=True)

"""## keys will be used to apply multi index dataframe."""

t1 = pd.concat([nov,dec],keys=['Nov','Dec'])
t1

t1.loc[('Dec',4)]

students.merge(t1,how='inner',on='student_id')

courses.merge(t1,how='left',on='course_id')

"""## Practice questions"""

# find total revenue generated

courses.merge(t1,how='inner',on='course_id')['price'].sum()

# find month by month revenue

temp_df = pd.concat([nov,dec],keys=['Nov','Dec']).reset_index()
temp_df.merge(courses,how='inner',on='course_id').groupby('level_0')['price'].sum()

temp_df1[temp_df1['level_0'] == 'Nov'].groupby('level_0')['price'].sum()

temp_df1[temp_df1['level_0'] == 'Dec'].groupby('level_0')['price'].sum()

# print the regristration table
# name -> course -> price

t1.merge(students,on='student_id').merge(courses,on='course_id')[['name','course_name','price']]

t1.merge(courses,on='course_id').groupby('course_name')['price'].sum().plot(kind='bar')

# find student who enrollned in both month

common_id = np.intersect1d(nov['student_id'],dec['student_id'])

students[students['student_id'].isin(common_id)]

# course that got no enrollment

no_enroll = np.setdiff1d(courses['course_id'],t1['course_id'])

courses[courses['course_id'].isin(no_enroll)]

# print student name and their partner name

students.merge(students,how = 'inner',left_on='partner',right_on='student_id')[['name_x','name_y']]

# top 3 students name who has most enrollments

t1.merge(students,on='student_id').groupby(['student_id','name'])['name'].count().sort_values(ascending=False).head(3)

import pandas as pd

matches = pd.read_csv('/content/matches.csv')
delivery = pd.read_csv('/content/deliveries (2).csv')

"""## Multi Index series and Data frame

# Why a series is 1d and dataframe is 2d?

bcz in series if we wnat an information we can fetch it by using 1 items

and in dataframe if we want to fetch information we need 2 items
"""

# The solution -> multiindex series(also known as Hierarchical Indexing)
# multiple index levels within a single index

# how to create multiindex object
# 1. pd.MultiIndex.from_tuples()
index_val = [('cse',2019),('cse',2020),('cse',2021),('cse',2022),('ece',2019),('ece',2020),('ece',2021),('ece',2022)]
multiindex = pd.MultiIndex.from_tuples(index_val)
multiindex.levels[1]
# 2. pd.MultiIndex.from_product()
pd.MultiIndex.from_product([['cse','ece'],[2019,2020,2021,2022]])

# creating a series with multiindex object
l1 = pd.Series([1,2,3,4,5,6,7,8],index=multiindex)
l1

# how to fetch items from series

l1['cse']

# to convert a multiindex into DataFrame we use unstach

l1.unstack()

branch_df1 = pd.DataFrame(
    [
        [1,2],
        [3,4],
        [5,6],
        [7,8],
        [9,10],
        [11,12],
        [13,14],
        [15,16],
    ],
    index = multiindex,
    columns = ['avg_package','students']
)

branch_df1

branch_df1['students']

branchdf_2 = pd.DataFrame(

    [[1,2,3,4],
    [5,6,7,8],
    [0,9,0,0],
    [0,0,0,0]],


    index = ['2019','2020','2021','2022'],

    columns = pd.MultiIndex.from_product([['delhi','mumbai'],['average_pkg','student']])
)

branchdf_2

"""## Above given data is 4d data. Still we can intrepret it as a 2d  using multiindex

# so advantage of multiindex is to present higher dimension data in lower dimention.
"""

branch_df1

## unstack : will convert index to column

branch_df1.unstack().unstack()

# stack :  will convert column to index

branch_df1.stack()

"""## Working with MultiIndex


"""

# head and tail
branch_df1.head()
# shape
branch_df1.shape
# info
branch_df1.info()
# duplicated -> isnull
branch_df1.duplicated()
branch_df1.isnull()

# how to access specific column from given dataset
branchdf_2.loc[('2019','delhi')]

# it will not give similar index in one tuple

branchdf_2.loc[('2019'):('2021'):2]

branchdf_2.iloc[:,1:3]

# extracting both row and column

branchdf_2.loc[('2019'):('2021'):2,('delhi','average_pkg')]

"""## Long VS Wide data

**Wide format** is where we have a single row for every data point with multiple columns to hold the values of various attributes.

**Long format** is where, for each data point we have as many rows as the number of attributes and each row contains the value of a particular attribute for a given data point.
"""

# melt -> simple example branch
# wide to long
pd.DataFrame({'cse':[120]}).melt()

pd.DataFrame({'cse':[120],'ece':[100],'mech':[50]})

# melt -> branch with year
pd.DataFrame({'cse':[120],'ece':[100],'mech':[50]}).melt(var_name='branch',value_name='num_students')

pd.DataFrame(
    {
        'branch':['cse','ece','mech'],
        '2020':[100,150,60],
        '2021':[120,130,80],
        '2022':[150,140,70]
    }
).melt(id_vars=['branch'],var_name='year',value_name='students')

death = pd.read_csv('/content/time_series_covid19_deaths_global.csv')
confirm = pd.read_csv('/content/time_series_covid19_confirmed_global.csv')

death.head(4)

confirm.head(4)

death = death.melt(id_vars=['Province/State','Country/Region','Lat','Long'],var_name='date',value_name='num_deaths')
confirm = confirm.melt(id_vars=['Province/State','Country/Region','Lat','Long'],var_name='date',value_name='num_cases')

confirm.merge(death,on=['Province/State','Country/Region','Lat','Long','date'])[['Country/Region','date','num_cases','num_deaths']]

"""## Practice questions"""

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Score": [85, 92, 88, None, 70],
    "Attempts": [1, 3, 2, 3, 1],
    "Qualified": ["Yes", "Yes", "No", "No", "Yes"]
}
df = pd.DataFrame(data)
df

# Find rows where the score is greater than 80.
df[df['Score'] > 80]

# Fill missing values in the Score column with the mean of the column.
df['Score'] = df['Score'].fillna(df['Score'].mean())
df

#Add a column Category with "High" if the score is above 90 and "Low" otherwise.
df['Category'] = df['Score'].apply(lambda x: 'High' if x>90 else 'Low')
df

data = {
    "Department": ["HR", "IT", "HR", "IT", "Finance"],
    "Salary": [50000, 60000, 55000, 65000, 70000],
    "EmployeeID": [1, 2, 3, 4, 5]
}
df = pd.DataFrame(data)
df

# Calculate the average salary by department.
df.groupby('Department')['Salary'].mean()

# Find the department with the highest total salary.
df.groupby('Department')['Salary'].sum().sort_values(ascending=False).head(1)

df1 = pd.DataFrame({
    "EmployeeID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"]
})

df2 = pd.DataFrame({
    "EmployeeID": [2, 3, 4],
    "Department": ["IT", "HR", "Finance"]})

# Perform an inner join to combine the two DataFrames on EmployeeID.
df1.merge(df2,on='EmployeeID')

#Perform a left join and identify employees who do not have a department.
left_join = df1.merge(df2,how='left',on='EmployeeID')
no_dept = left_join[left_join['Department'].isna()]
no_dept

data = {
    "ID": [1, 1, 2, 2],
    "Year": [2020, 2021, 2020, 2021],
    "Sales": [200, 250, 300, 350]
}
df = pd.DataFrame(data)
df

# Reshape the data to have years as columns.
reshaped = df.pivot(index="ID", columns="Year", values="Sales")
print("Reshaped DataFrame:")
print(reshaped)



