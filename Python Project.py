#!/usr/bin/env python
# coding: utf-8

# ## How many are there in each Team and the percentage splitting with respect to the total employees.

# In[1]:


import pandas as pd

df = pd.read_csv('myexcel.csv')
team_counts = df.groupby('Team')['Name'].value_counts()
total_emp = len(df)
team_percent = (team_counts / total_emp) * 100

print("Number of employees in each team:")
print(team_counts)

print("\nPercentage of employees in each team:") 
print(team_percent)




# # Segregate the employees w.r.t different positions.

# In[2]:


import pandas as pd

df = pd.read_csv('myexcel.csv') 

positions = df['Position'].unique()

for position in positions:
    position_df = df[df['Position'] == position]
    print(f"\n{position}")
    
    for index, row in position_df.iterrows():
        print(row['Name'])


# # Find from which age group most of the employees belong to.

# In[3]:


bins = [20, 25, 30, 35, 40, 45, 50, 55]
labels = ['20-25', '25-30', '30-35', '35-40', '40-45', '45-50', '50+']
df['AgeGroup'] = pd.cut(df['Age'], bins, labels=labels)
age_grp = df['AgeGroup'].value_counts()
print(age_grp)
max_age = age_grp.idxmax()
print(max_age)


# ## Find out under which team and position, spending in terms of salary is high.

# In[4]:


df = pd.read_csv('myexcel.csv')

grouped = df.groupby(['Team', 'Position'])

avg_sal = grouped['Salary'].mean().reset_index()

max_sal = avg_sal[avg_sal['Salary'] == avg_sal['Salary'].max()]

print(max_sal[['Team', 'Position']])


# # Find if there is any correlation between age and salary , represent it visually.

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('myexcel.csv') 


plt.scatter(df['Age'], df['Salary'])


plt.xlabel('Age')  
plt.ylabel('Salary')


corr = df['Age'].corr(df['Salary'])
print('Correlation:', corr)

plt.show()

