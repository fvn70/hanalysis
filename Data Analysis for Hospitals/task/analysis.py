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
print(f'Data shape: {df_all.shape}')
# Print random 20 rows
print(df_all.sample(n=20, random_state=30))
