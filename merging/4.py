import pandas as pd

def convert_dtype(x):
    if not x:
        return ''
    try:
        return str(x)
    except:
        return ''

# Read in the CSV files
df1 = pd.read_csv('1_copy.csv', converters={'age': convert_dtype,'tahol': convert_dtype, 'tahsilat': convert_dtype,
                                           'fesharekhoon': convert_dtype, 'hamlegalbi': convert_dtype, 'sektemagzi': convert_dtype,
                                           'saratan': convert_dtype, 'asm': convert_dtype, 'kamkhooni': convert_dtype,
                                           'charbiekhoon': convert_dtype, 'kabedcharb': convert_dtype})

df2 = pd.read_csv('output.csv', converters={'sex': convert_dtype,'codkhooshe': convert_dtype,'codkhanevar': convert_dtype
                                            ,'age': convert_dtype,'tahol': convert_dtype,'tahsilat': convert_dtype
                                            ,'diabet': convert_dtype,'ezterab': convert_dtype,'fesharekhoon': convert_dtype
                                            ,'hamlegalbi': convert_dtype,'sektemagzi': convert_dtype,'saratan': convert_dtype
                                            ,'asm': convert_dtype,'kamkhooni': convert_dtype,'charbiekhoon': convert_dtype
                                            ,'kabedcharb': convert_dtype})



# Iterate over the columns in file 2
for column in df2.columns:
    # Check if the column exists in file 1
    if column in df1.columns:
        # Add any extra data from file 2 to file 1
        df1[column] = df2[column].combine_first(df1[column])

# Save the merged dataframe to a new CSV file
df1.to_csv('1final.csv', index=False)