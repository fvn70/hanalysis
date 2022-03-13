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
# Print random 20 rows
print(df_all.sample(n=20, random_state=30))
