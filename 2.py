## merging 2 datasets based on their differences
import pandas as pd

# Read the 1 and 2 CSV files
df1 = pd.read_csv('1.csv', low_memory=False)

df2 = pd.read_csv('2.csv', low_memory=False)

# Make a copy of the 2 DataFrame
df2_copy = df2.copy()

# Specify the columns to copy from df1 to df2_copy
cols_to_copy = ['BMI', 'BMIrotbe', 'GADkoll', 'GADrotbe', 'HDLlowwww', 'LDLbala', 'LDLrotbe', 'NTI001', 'Physicalactiv', 'TGbala', 'TGrotbe', 'WbeHmardan', 'WbeHzanann', 'age10sal', 'anemia', 'chgh', 'cholebala', 'cholrotbe', 'conicityindex', 'creatinedr', 'creatinimmol', 'diabetcas', 'diabeti', 'diasrotb', 'dorekamarbala', 'dorkamarbebasan', 'dyslipd', 'ezafechagh', 'ezafevazn', 'faaliat', 'feshartotal', 'feshrdarj2', 'filter_$', 'gandsara', 'hyper1', 'hyper2', 'intersalt', 'intersaltgr', 'kamarmardan', 'kamarzanan', 'metabolicsyndrome', 'nacldariaftipredictiv', 'naclpredbala', 'potasiuedr', 'prcr24', 'prehyper', 'proffetion', 'ros2tagir', 'ros5tagir', 'rosegradeee', 'rosmosbat', 'saranemasrafenamak', 'saranenamak', 'saranenamakbala', 'saranenamakk', 'saranesang4', 'saranesangnamak', 'saranrogan', 'saranrogjamed', 'saranrogmaie', 'saranrognimejamed', 'serumvitDrotb', 'shahrepurmia', 'shahrroosta', 'shekarsara', 'shekarvagandsara', 'sisrotbe', 'sodiuedra', 'sodium24edr', 'vitDserkam', 'waisttoheight', 'waisttoheightratio']

# Copy the specified columns from df1 to df2_copy
df2_copy[cols_to_copy] = df1[cols_to_copy]

# Save the modified df20_copy to a new CSV file
df2_copy.to_csv('2_copy.csv', index=False)

# Make a copy of df_1
df1_copy = df1.copy()

# Select the columns to copy from df_2 to df_1_copy
cols_to_copy = ['FAC1_1', 'FAC2_1', 'FAC3_1', 'RFAC1_1', 'RFAC2_1', 'RFAC3_1']

# Copy the selected columns from df_20 to df_17_copy
df1_copy[cols_to_copy] = df2[cols_to_copy]

# Save the modified df_17_copy to a new csv file
df1_copy.to_csv('1_copy.csv', index=False)