import pandas as pd

pd.set_option('display.max_columns', 8)
df_gen = pd.read_csv('test/general.csv')
df_pre = pd.read_csv('test/prenatal.csv')
df_spo = pd.read_csv('test/sports.csv')
print(df_gen.head(20))
print(df_pre.head(20))
print(df_spo.head(20))
