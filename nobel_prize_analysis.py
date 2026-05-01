#import pandas to read csv file
import pandas as pd 

#visaulization
import seaborn as sns

nobel = pd.read_csv('data/nobel.csv')

#most commonly awarded gender and birth country
top_gender = nobel['sex'].mode()[0]
top_country = nobel['birth_country'].mode()[0]


#assign years into decades and where birth country is USA
nobel['decade'] = (nobel['year'] // 10) * 10
nobel['usa_born_winners'] = nobel['birth_country'] == 'United States of America'

# Calculate ratio of US-born winners per decade
usa_ratio = nobel.groupby('decade', as_index=False)['usa_born_winners'].mean()

# Find decade with highest ratio
max_decade_usa = usa_ratio.loc[usa_ratio['usa_born_winners'].idxmax(), 'decade']

#Plotting USA born winners
ax1 = sns.relplot(x='decade', y='usa_born_winners', data= usa_ratio, kind="line")

#decade and Nobel Prize category combination with the highest proportion of female laureates
nobel['Female_Laureates'] = (nobel['category'] == 'Literature') & (nobel['sex'] == 'Female')

# Calculate proportion of female laureates by decade and category
female_ratio = nobel.groupby(
    ['decade', 'category'], as_index=False
)['Female_Laureates'].mean()

# Find row with highest proportion
top_row = female_ratio.loc[female_ratio['Female_Laureates'].idxmax()]

# Store as dictionary
max_female_dict = {top_row['decade']: top_row['category']}

#Plotting female winners with % winners on the y-axis
ax2 = sns.relplot(x='decade', y='Female_Laureates', hue='category', data = female_ratio, kind="line")

# Filter only female winners
female_winners = nobel[nobel['sex'] == 'Female']

# Sort by year (earliest first)
first_woman = female_winners.sort_values('year').iloc[0]

#save answers
first_woman_name = first_woman['full_name']
first_woman_category = first_woman['category']

# Count how many times each full_name appears
name_counts = nobel['full_name'].value_counts()

#individuals or organizations have won more than one Nobel Prize throughout the years

# Select only those who appear more than once
repeat_winners = name_counts[name_counts > 1]

# Store as a list
repeat_list = repeat_winners.index.tolist()








