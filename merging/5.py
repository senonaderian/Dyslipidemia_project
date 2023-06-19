import pandas as pd

# Read in the two CSV files
df1 = pd.read_csv("1final.csv", low_memory=False)
df2 = pd.read_csv("ffq.csv", low_memory=False)

# Get the set of column names in each file
set1 = set(df1.columns)
set2 = set(df2.columns)

# Find the differences in the column names
diff1 = sorted(set1 - set2)
diff2 = sorted(set2 - set1)

# Print the results
if diff1:
    print(f"file1 has columns {diff1} that file2 doesn't have")
if diff2:
    print(f"file2 has columns {diff2} that file1 doesn't have")
