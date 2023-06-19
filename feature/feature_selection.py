from sklearn.impute import SimpleImputer
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('minmax_normalized_data.csv')

# Extract the 'dyslipd' column and store it in a separate variable
target = df['dyslipd']

# Select all columns except for the 'TGrotbe' column
data = df.drop('dyslipd', axis=1)

# Impute missing values with mean
imputer = SimpleImputer(strategy='mean')
data_imputed = imputer.fit_transform(data)

# Create a SelectKBest object using chi2 score function and fit to data
from sklearn.feature_selection import SelectKBest, chi2
selector_chi2 = SelectKBest(chi2, k=10)
X_chi2 = selector_chi2.fit_transform(data_imputed, target)

# Print selected features using chi2 score function
print("Selected Features (using chi-square score function):")
selected_features_chi2 = data.columns[selector_chi2.get_support()]
print(selected_features_chi2)

# Create a SelectKBest object using mutual_info_classif score function and fit to data
from sklearn.feature_selection import mutual_info_classif
selector_mi = SelectKBest(mutual_info_classif, k=10)
X_mi = selector_mi.fit_transform(data_imputed, target)

# Print selected features using mutual_info_classif score function
print("Selected Features (using mutual information score function):")
selected_features_mi = data.columns[selector_mi.get_support()]
print(selected_features_mi)

# Create a SelectKBest object using f_classif score function and fit to data
from sklearn.feature_selection import f_classif
selector_f_classif = SelectKBest(f_classif, k=10)
X_f_classif = selector_f_classif.fit_transform(data_imputed, target)

# Print selected features using f_classif score function
print("Selected Features (using f_classif score function):")
selected_features_f_classif = data.columns[selector_f_classif.get_support()]
print(selected_features_f_classif)
