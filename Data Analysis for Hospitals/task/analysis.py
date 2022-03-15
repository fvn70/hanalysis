import pandas as pd

pd.set_option('display.max_columns', 8)

df_gen = pd.read_csv('test/general.csv')
df_pre = pd.read_csv('test/prenatal.csv')
df_spo = pd.read_csv('test/sports.csv')

# Change the column names
heads = df_gen.columns
df_pre.columns = heads
df_spo.columns = heads
# Merge the data frames into one.
df_all = pd.concat([df_gen, df_pre, df_spo], ignore_index=True)
# Delete the Unnamed: 0 column
df_all.drop(columns='Unnamed: 0', inplace=True)
# Delete all the empty rows
df_all.dropna(how='all', inplace=True)
# Correct all the gender column values to f and m
df_all.gender = df_all.gender.replace('ma.+', 'm', regex=True)
df_all.gender = df_all.gender.replace(r'[fw].*', 'f', regex=True)
# Replace the NaN values in the gender column of the prenatal hospital with f
df_all.gender = df_all.gender.fillna('f')
# Replace the NaN values in the bmi ... months columns with zeros
zeros = {'bmi': 0, 'diagnosis': 0, 'blood_test': 0, 'ecg': 0, 'ultrasound': 0, 'mri': 0, 'xray': 0, 'children': 0, 'months': 0}
df_all.fillna(value=zeros, inplace=True)
# print(f'Data shape: {df_all.shape}')
# Print random 20 rows
# print(df_all.sample(n=20, random_state=30))

# 1. Which hospital has the highest number of patients?
ans1 = df_all.hospital.value_counts().idxmax()
print(f'The answer to the 1st question is {ans1}')
# 2. What share of the patients in the general hospital suffers from stomach-related issues?
df_gen = df_all.loc[df_all['hospital'] == 'general']
val = df_gen.loc[df_gen['diagnosis'] == 'stomach'].shape[0] / df_gen.shape[0]
print(f'The answer to the 2nd question is {round(val, 3)}')
# 3. What share of the patients in the sports hospital suffers from dislocation-related issues?
df_spo = df_all.loc[df_all['hospital'] == 'sports']
val = df_spo.loc[df_spo['diagnosis'] == 'dislocation'].shape[0] / df_spo.shape[0]
print(f'The answer to the 3rd question is {round(val, 3)}')
# 4. What is the difference in the median ages of the patients in the general and sports hospitals?
val = df_gen.age.median() - df_spo.age.median()
print(f'The answer to the 4th question is {round(val, 3)}')
# 5. In which hospital the blood test was taken the most often
df_bl = df_all.loc[df_all['blood_test'] == 't']
d = df_bl.groupby(['hospital']).agg({'blood_test': 'count'})
print(f'The answer to the 5th question is {d.idxmax()[0]}, {d.agg(max)[0]} blood tests')
