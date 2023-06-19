import pandas as pd

# Read the first CSV file
df1 = pd.read_csv('2_copy.csv')

# Read the second CSV file
df2 = pd.read_csv('1_copy.csv')

# Get the column order from the second CSV file
desired_columns = df2.columns

# Rearrange the columns of the first dataframe based on the desired order
df1 = df1[desired_columns]

# Save the rearranged dataframe to a new CSV file
df1.to_csv('output.csv', index=False)
