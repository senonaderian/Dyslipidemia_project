## merging 2 datasets based on their differences
import pandas as pd

# Read the 1 and 2 CSV files
df1 = pd.read_csv('1final.csv', low_memory=False)

df2 = pd.read_csv('ffq.csv', low_memory=False)

# Make a copy of the 2 DataFrame
df2_copy = df2.copy()

# Specify the columns to copy from df1 to df2_copy
cols_to_copy = ['BMI', 'BMIrotbe', 'GADkoll', 'GADrotbe', 'HDLlowwww', 'LDLbala', 'LDLrotbe', 'NTI001', 'Physicalactiv', 'TGbala', 'TGrotbe', 'WbeHmardan', 'WbeHzanann', 'age10sal', 'anemia', 'chgh', 'cholebala', 'cholrotbe', 'conicityindex', 'creatinedr', 'creatinimmol', 'diabetcas', 'diabeti', 'diasrotb', 'dorekamarbala', 'dorkamarbebasan', 'dyslipd', 'ezafechagh', 'ezafevazn', 'faaliat', 'feshartotal', 'feshrdarj2', 'filter_$', 'gandsara', 'hyper1', 'hyper2', 'intersalt', 'intersaltgr', 'kamarmardan', 'kamarzanan', 'metabolicsyndrome', 'nacldariaftipredictiv', 'naclpredbala', 'potasiuedr', 'prcr24', 'prehyper', 'proffetion', 'ros2tagir', 'ros5tagir', 'rosegradeee', 'rosmosbat', 'saranemasrafenamak', 'saranenamak', 'saranenamakbala', 'saranenamakk', 'saranesang4', 'saranesangnamak', 'saranrogan', 'saranrogjamed', 'saranrogmaie', 'saranrognimejamed', 'serumvitDrotb', 'shahrepurmia', 'shahrroosta', 'shekarsara', 'shekarvagandsara', 'sisrotbe', 'sodiuedra', 'sodium24edr', 'vitDserkam', 'waisttoheight', 'waisttoheightratio']
# Copy the specified columns from df1 to df2_copy
df2_copy[cols_to_copy] = df1[cols_to_copy]

# Save the modified df20_copy to a new CSV file
df2_copy.to_csv('ffqcopy.csv', index=False)
