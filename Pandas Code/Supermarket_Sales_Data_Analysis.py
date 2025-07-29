import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# --------------------------
# # TASK-6 -> Regional Profitability Analysis
##[Log Entry 9]

# #Used a dictionary to apply different aggregation function to different columns.
# agg_dict = { 'Profit ($-USD)': 'mean', 'Sales ($-USD)': 'sum'}
# #Grouped the data by region and aggregated the mean profit and total sales for each region.
# task_6_df_grouped = df.groupby('Region').agg(agg_dict).reset_index()
# #Sorted the values by Profit in their descending order.
# task_6_sorted = task_6_df_grouped.sort_values(by='Profit ($-USD)', ascending=False)
# print(task_6_sorted)
# print('---------')
# #Now similarly, calculating the total Profit and Sales, then deriving Profit Margin
# agg_dict2 = { 'Profit ($-USD)': 'sum', 'Sales ($-USD)': 'sum'}
# p_df = df.groupby('Region').agg(agg_dict2).reset_index()
# # # Created a new column, "Profit Margin (%)", which is the result of dividing total profit by total Sales (revenue).
# p_df['Profit Margin (%)'] = (p_df['Profit ($-USD)']/ p_df['Sales ($-USD)']) * 100
# # #The data is sorted in descending order to get the region with the highest profit margin.
# p_df_sorted = p_df.sort_values(by='Profit Margin (%)', ascending = False)
# print(p_df_sorted)

# ##[Log Entry 10]

# ##Plotting a bar graph using seaborn.
# sns.barplot(
#      data=p_df,
#      x='Region',
#      y='Profit Margin (%)',
#      hue='Region',
#      palette='pastel'
# )
# plt.title("Profit Margin by Region", fontsize='14', fontweight='medium')
# plt.ylabel("Profit Margin (%)", fontsize=12)
# plt.xlabel("Region", fontsize=12)
# plt.tight_layout()
# #plt.savefig('task-6-bar-graph-seaborn.png')
# plt.show()

# --------------------------
# ## TASK-7 -> Discount Impact on Profitability

# agg_dict_task7 = { 'Profit ($-USD)':'sum', 'Sales ($-USD)':'sum'}
# #Grouped the data by Discount and calculated total Profit and Sales.
# task_7_df_grouped = df.groupby(['Discount']).agg(agg_dict_task7).reset_index()
# print(task_7_df_grouped)
# #[Log Entry 11]

# #Plotting a regression graph using seaborn.
# sns.regplot(data=task_7_df_grouped,
#              x='Discount',
#              y='Profit ($-USD)',
#              scatter_kws={'alpha':0.5}, color='orange')
#
# plt.title('Profit Distribution by Discount Level')
# plt.xlabel('Discount (%)')
# plt.ylabel('Total Profit ($-USD)')
# plt.tight_layout()
# # plt.savefig('task-7-regression-plot-seaborn.png')
# plt.show()
