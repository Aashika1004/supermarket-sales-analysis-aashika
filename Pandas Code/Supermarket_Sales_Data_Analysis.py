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

##------------------------------
##TASK-2 -> For each state, find only the top-performing sub-category, based on total sales.
##[Log Entry 4]

# #Using groupby to group required columns and then using .sum() aggregation function for Sales column, finally using reset_index to turn the result into DataFrame.
# task_2_df_unsorted = df.groupby(['State','Sub-Category'])['Sales ($-USD)'].sum().reset_index()

# #Sorting the dataset by State column in ascending order, then by the Sales column in descending order
# task_2_df_sorted = task_2_df_unsorted.sort_values(by=['State', 'Sales ($-USD)'], ascending=[True, False])

# #Removing the duplicated values by only taking the first row of each state (which would be the highest selling product per state)
# task_2_df = task_2_df_sorted.drop_duplicates(subset='State', keep='first')
# print(task_2_df)

# #[Log Entry 5]

##------------------------------
##TASK - 3 - Percentage of Standard vs. Second Class Shipments

# #Used counts to count each occurrence of the shipment modes, used 'normalize' for % proportions and multiplied by 100 for readability.
# task_3_df = df.value_counts(subset='Ship Mode', normalize=True) * 100
# print(task_3_df)

# #[Log Entry 6]

# #Plotting the Pie chart using matplotlib
# mylabels=task_3_df.index
# plt.pie(task_3_df, labels = mylabels)
# plt.title('Percentage of Standard vs. Second Class Shipments')
# plt.legend(loc='lower left', bbox_to_anchor=(0.9, 0.5))
# #plt.savefig('task-3-pie-chart-matplotlib.png')
# plt.show()

# --------------------------

##TASK - 4 -> Compare Corporate vs. Consumer Customers

# #Grouping by segment and then using .sum() aggregate function to get the total sales per segment.
# task_4_df_sum = df.groupby('Segment')['Sales ($-USD)'].sum().reset_index()
# #Average order value by segment.
# task_4_df_mean = df.groupby('Segment')['Sales ($-USD)'].mean()
# print(task_4_df_sum)
# print("------")
# print(task_4_df_mean)

##[Log Entry 7]

# --------------------------
## TASK-5 -> Identify top-performing sub-categories/products

# #Grouping by Sub-Category and calculating total sales per Sub-Category
# task_5_df_grouped = df.groupby('Sub-Category')['Sales ($-USD)'].sum().reset_index()
# #Sorting the values in descending order
# task_5_df_sorted = task_5_df_grouped.sort_values('Sales ($-USD)', ascending=False)
# print(task_5_df_sorted)

##[Log Entry 8]
