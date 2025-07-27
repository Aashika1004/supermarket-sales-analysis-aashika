import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('SampleSuperstore.csv')
# Formatting floats for better readability of figures
pd.set_option('display.float_format', '{:,.2f}'.format)
# Renaming few columns for clarity
df.rename(columns={
    'Profit': 'Profit ($-USD)',
    'Sales': 'Sales ($-USD)'
}, inplace=True)

##TASK-1 -> Analyze total sales per product category

## [NOTE] The following statements are only for Column review and Pre-Analysis checks.
##        These are not intended to be part of the main analysis pipeline.
##Checking if there is any missing data in the dataset
# print(df.isnull().sum())
# Reviewing the columns needed for Data Analysis through isolation.
# print(df[['Category','Sub-Category','Sales ($-USD)']])
# Grouping the required columns together - First Check
##[Log Entry 1]
# grouped_data = df.groupby(['Category', 'Sub-Category', 'Sales ($-USD)'])
# #print(grouped_data)
## [NOTE] End of Pre-check -> Task 1 Begins

# #[Log Entry 2]
#Using groupby to group required columns and sum for aggregation, finally using reset_index to turn result into DataFrame.
task_1_df = df.groupby(['Category', 'Sub-Category'])['Sales ($-USD)'].sum().reset_index()
print(task_1_df)

# #[Log Entry 3]

# #Plotting the bar using matplotlib
# #Using horizontal bar graph since there are many sub-categories
# plt.barh(task_1_df['Sub-Category'], task_1_df['Sales ($-USD)'])
# plt.ylabel('Sub-Category')
# plt.xlabel('Total Sales ($-USD)')
# plt.title('Total Sales ($-USD) per Product Category')
# #plt.savefig('task-1-graph-matplotlib.png')
# plt.show()
