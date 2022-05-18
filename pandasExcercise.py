import matplotlib.pyplot as plt
import pandas as pd

# 4. Python 4 Data Science Excercise #
######################################

# (1) read dataframe
url = 'https://raw.githubusercontent.com/edlich/eternalrepo/3b284c8cad5433c81950bac84876fcbfc5de4f36/DS-WAHLFACH/countries.csv'
df = pd.read_csv(url)
# df = pd.read_csv('countries.csv', delimiter=';')

# (2) Display some informations
print('\n Ausgabe Dataframe')
print(df)
print('\n Statistische basis informationen')
print('Spaltennamen')
col_names = list(df.columns.values)
print(col_names)
print('Datentypen je Spalte')
print(df.dtypes)
print('Größen informatin')
print(df.shape)
print(df.describe())
df2 = df.drop(['Name', 'BIP', 'Currency'], axis=1)
print(df2)
df2.plot()
# plt.show()

# (3) Show the last 4 rows of the data frame.
print('\n die letzten 4 Zeilen')
#df3 = df.drop(0)
df3 = df[-4:]
print(df3)

# (4) Show all the row of countries who have the EURO
print('\n Zeilen die Currency mit EUR')
df_euro = df.loc[df['Currency'] == 'EUR']
print(df_euro)

# (5) Show only name and Currency in a new data frame
print('\n zeige nur die Spalte Currency')
#df4 = df.drop(['Name', 'BIP', 'Area', 'People'], axis=1)
df4 = df['Currency']
print(df4)

# (6) Show only the rows/countries that have more than 2000 BIP (it is in Milliarden USD Bruttoinlandsprodukt)
print('\n Zeige nur Zeilen deren Bip > 2000')
df_bip = df.loc[df['BIP'] >= 2000]
print(df_bip)

# (7) Select all countries where with inhabitants between 50 and 150 Mio
print('\n Länder deren EW-zahl zwischen 50 und 150 Mio. liegt')
df_people = df[df['People'].between(50000000, 150000000)]
print(df_people)

# (8) Change BIP to Bip
print('\n rename BIP to bip')
df_new = df.rename(columns={'BIP': 'Bip'})
print(list(df_new.columns.values))

# (9) Calculate the Bip sum
print('\n die Summe von Bip')
bip_sum = df_new['Bip'].sum()
print(bip_sum)

# (10) Calculate the average people of all countries
print('\n die Durschnittliche Bevölkerung aller Länder beträgt:')
mean_people = df_new['People'].mean()
print(mean_people)

# (11) Sort by name alphabetically
print('\n data sortiert nach Namen asc')
df_sort = df_new.sort_values(by='Name')
print(df_sort)

# (12) Create a new data frame from the original where the area is changed as follows:
# all countries with > 1000000 get BIG and <= 1000000 get SMALL in the cell replaced!
print('\n rename area values to small and big')
df_small = df_new['Area'] <= 1000000
df_big = df_new['Area'] > 1000000
df_new.loc[df_small, 'Area'] = 'SMALL'
df_new.loc[df_big, 'Area'] = 'BIG'
print(df_new)


